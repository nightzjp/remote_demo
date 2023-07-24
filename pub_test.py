import uuid
import datetime

# GPS数据结构
gps_xml_0 = f"""
<HiATMP id="GPSINF">
    <GPS>
        <VEHCODE id="终端编号">
            DECARLON: 经度,
            DECARLAT: 维度,
            NCARSTATUS: 车辆启动状态,
            NDIRECTION: 方向,
            NVEHSPEED: 速度,
            NVEHALARM: 报警信息编号,
            DTRECORDTIME: 采集时间
        </VEHCODE>
    </GPS>
</HiATMP>
"""

# GPS数据示例
gps_xml_1 = f"""
<HiATMP id="GPSINF">
    <GPS>
        <VEHCODE id="{'0001'}">
            {'104.10194'},
            {'30.65984'},
            {'1'},
            {'4'},
            {'30'},
            {'4'},
            {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        </VEHCODE>
    </GPS>
</HiATMP>
"""


# 违章数据结构
illegal_0 = f"" \
            f"{'接口类型: ILLEGAL04'}," \
            f"{'接口版本: 2.5'}," \
            f"{'厂商ID: 0099'}," \
            f"{'MSGID: UUID'}," \
            f"{'违法数据来源: 9'}," \
            f"{'号牌种类：附录'}," \
            f"{'号牌号码: 识别到的号牌'}," \
            f"{'采集时间: YYYY-MM-DD HH:MM:SS'}," \
            f"{'违法代码: 参考公安标准'}," \
            f"{'采集点编号: 参考'}," \
            f"{'采集地址: 地址'}," \
            f"{'采集机关代码: 12位'}," \
            f"{'数据来源: 参考'}," \
            f"{'抓拍类型：1'}," \
            f"{'设备编号: 参考'}," \
            f"{'方向编号: 参考'}," \
            f"{'证据图片1：图片URL'}," \
            f"{'证据图片2：图片URL'}," \
            f"{'证据图片3：图片URL'}," \
            f"{'执勤民警：警号'}," \
            f"{'触发决定书编号：15位'}," \
            f"{'视频证据：URL-5秒视频'}," \
            f"{'号牌特征信息：附录'}," \
            f"{'号牌颜色：附录'}," \
            f"{'数据上传时间：YYYY-MM-DD HH：MM：SS'}," \
            f"{'是否已审：0'}," \
            f"{'车道编号：参考'}"

# 违章数据示例
# ILLEGAL01,2.4,0002,7eca4af22a3711eeb8a1d5dfb59bd1ea,1,02,粤XXXXX,2023-07-24 15:32:44,1117,000011013000,XXXXX路口,440703000000,01,1,440703000000010448,1,02,,0,ftp://XX:XX@44.111.11.110:21/weifa/1/weifa/2023/07/24/15/2-20230724153244280-weifa-1117-(1).jpg,ftp://XX:XX@44.111.11.110:21/weifa/1/weifa/2023/07/24/15/2-20230724153245561-weifa-1117-(2).jpg,ftp://XX:XX@44.111.11.110:21/weifa/1/weifa/2023/07/24/15/2-20230724153340980-weifa-1117-(3).jpg,ftp://XX:XX@44.111.11.110:21/weifa/1/weifa/2023/07/24/15/2-20230724153245561-weifa-1117-(2).avi,2400/2067/168/46/1,2,2023-07-24 15:33:53,0
illegal_1 = f"" \
            f"{'ILLEGAL01'}," \
            f"{'2.5'}," \
            f"{'0099'}," \
            f"{str(uuid.uuid4()).replace('-', '')}," \
            f"{'9'}," \
            f"{'02'}," \
            f"{'川A00001'}," \
            f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}," \
            f"{'1117'}," \
            f"{'000011013000'}," \
            f"{'四川省成都市天府机场XX路口'}," \
            f"{'440703000000'}," \
            f"{'05'}," \
            f"{'1'}," \
            f"{'440703000000010448'}," \
            f"{'0'}," \
            f"{'https://dm30webimages.lynkco.com.cn/LynkCoPortal/Files/2023/0707/PC3.jpg'}," \
            f"{'https://dm30webimages.lynkco.com.cn/LynkCoPortal/Files/2023/0707/PC3.jpg'}," \
            f"{'https://dm30webimages.lynkco.com.cn/LynkCoPortal/Files/2023/0707/PC3.jpg'}," \
            f"{'000000000000'}," \
            f"{'0123456789ABCDE'}," \
            f"{'https://dm30webimages.lynkco.com.cn/LynkCoPortal/Files/2023/0707/PC3.jpg'}," \
            f"{'819/1506/122/26/1'}," \
            f"{'绿'}," \
            f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}," \
            f"{'0'}," \
            f"{'000000'}"

print(gps_xml_1)
print(illegal_1)
