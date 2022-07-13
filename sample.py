# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import sys
import time

from typing import List
from Tea.core import TeaCore

from alibabacloud_dcdn20180115.client import Client as dcdn20180115Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dcdn20180115 import models as dcdn_20180115_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_console.client import Client as ConsoleClient
from alibabacloud_tea_util.client import Client as UtilClient


class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client(
        access_key_id: str,
        access_key_secret: str,
    ) -> dcdn20180115Client:
        """
        使用AK&SK初始化账号Client
        @param access_key_id:
        @param access_key_secret:
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config(
            # 您的 AccessKey ID,
            access_key_id=access_key_id,
            # 您的 AccessKey Secret,
            access_key_secret=access_key_secret
        )
        # 访问的域名
        config.endpoint = f'dcdn.aliyuncs.com'
        return dcdn20180115Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        #global ACCESS_KEY_ID

        ACCESS_KEY_ID = args[0]
        ACCESS_KEY_SECRET = args[1]
        object_path = args[2]
        object_type = args[3]

        client = Sample.create_client(ACCESS_KEY_ID, ACCESS_KEY_SECRET)
        # 刷新节点上的文件内容
        refresh_dcdn_object_caches_request = dcdn_20180115_models.RefreshDcdnObjectCachesRequest(
            object_path=object_path,
            object_type=object_type
        )
        runtime = util_models.RuntimeOptions()
        resp = client.refresh_dcdn_object_caches_with_options(refresh_dcdn_object_caches_request, runtime)
        ConsoleClient.log(UtilClient.to_jsonstring(TeaCore.to_map(resp.body)))
        RefreshTaskId = TeaCore.to_map(resp.body).get('RefreshTaskId')
        # return RefreshTaskId
        #print(RefreshTaskId)
        time.sleep(5)

        #获取刷新预热任务信息
        describe_dcdn_refresh_tasks_request = dcdn_20180115_models.DescribeDcdnRefreshTasksRequest(
            task_id = RefreshTaskId
        )
        runtime = util_models.RuntimeOptions()
        try:
            # 复制代码运行请自行打印 API 的返回值
            resp = client.describe_dcdn_refresh_tasks_with_options(describe_dcdn_refresh_tasks_request, runtime)
            ConsoleClient.log(UtilClient.to_jsonstring(TeaCore.to_map(resp.body)))
            #tasks = TeaCore.to_map(resp.body).get('Tasks')
            #print(tasks.get("Task")[0].get("Process"))

        except Exception as error:
            # 如有需要，请打印 error
            e = UtilClient.assert_as_string(error.message)
            print('\t---------------------------------------------\n', e)
if __name__ == '__main__':
    Sample.main(sys.argv[1:])


