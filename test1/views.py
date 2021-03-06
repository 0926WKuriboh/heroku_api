from test1.models import Data
from test1.serializers import DataSerializer
from test1.models import fund_datas, update_text, dbget_info_min, verify_account, check_hash

from rest_framework.decorators import action
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.http import HttpResponseRedirect
import json


def hello(request):
    return render(request, 'test.html')


class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer

    # permission_classes = (IsAuthenticated,)

    @action(methods=['get'], detail=True)
    def aa(self, request, pk=None):
        print(pk)
        data = get_object_or_404(Data, pk=pk)
        result = {
            'id': data.id
        }

        return Response(result, status=status.HTTP_200_OK)

    # 測試用
    @action(methods=['get'], detail=False)
    def raw_sql_query(self, request):
        ida = request.query_params.get('id', None)
        test1 = fund_datas(id=ida)
        serializer = DataSerializer(test1, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 更新資料用
    @action(methods=['put'], detail=False)
    def update_text(self, request, pk=None):
        print(request.data)
        id = request.query_params.get('id')
        print(request.query_params)
        category = request.data.get('category')
        tag = request.data.get('tag')
        display = request.data.get('display')
        data = update_text(id=id, category=category, tag=tag, display=display)
        return Response(data, status=status.HTTP_200_OK)

    # 拿後臺主頁資料
    @action(methods=['post'], detail=False)
    def get_info_min(self, request):
        longin_hash = request.data.get('hash')
        account = request.data.get('account')
        print(str(longin_hash))
        if check_hash(account, longin_hash):
            data = dbget_info_min()
            return Response(data, status=status.HTTP_200_OK)
        return Response(False, status=status.HTTP_200_OK)

    # 弄做登入用，輸入正確傳回帳號做hash
    @action(methods=['post'], detail=False)
    def login(self, request):
        account = request.data.get('account')
        password = request.data.get('password')
        result = verify_account(account=account, password=password)
        return Response(result, status=status.HTTP_200_OK)

    # 測試用
    @action(methods=['get'], detail=False)
    def request_test(self, request):
        return HttpResponseRedirect('https://ffbd6e99.ngrok.io/templates/test2')
