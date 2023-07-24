import datetime
import time

import stomp
from stomp.exception import ConnectFailedException

topic_name = "topic/SampleTopic"
topic_gps = "HIATMP.HISENSE.GPS"  # GPS
topic_pass = "HIATMP.HISENSE.PASS.PASSINF"  # 微卡口
topic_illegal = "HIATMP.HISENSE.ILLEGAL"  # 违章
host = "192.168.2.44"
port = 61613
listener_name = "listener_name"


class SampleListener(stomp.ConnectionListener):

    def on_message(self, message):
        print("message: %s" % message)


def send_to_topic(topic, message):
    """发送数据到topic"""
    try:
        conn = stomp.Connection(host_and_ports=[(host, port)], reconnect_attempts_max=2, timeout=1)
        conn.connect("admin", "admin", wait=True)
        # print(conn.is_connected())
        # print(topic, message)
        conn.send(topic, message)
    except ConnectFailedException:
        print("连接失败")
    else:
        conn.disconnect()


def receive_from_topic(topic):
    """从topic获取数据"""
    try:
        conn = stomp.Connection(host_and_ports=[(host, port)], reconnect_attempts_max=2, timeout=1)
        conn.set_listener(listener_name, SampleListener())
        conn.connect("admin", "admin", wait=True)
        conn.subscribe(topic, id="client_id")
        time.sleep(3)
    except ConnectFailedException:
        print("连接失败")
    else:
        conn.disconnect()


if __name__ == '__main__':
    gps_xml = f"""
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
    illegal0 = f"{'接口类型: ILLEGAL04'},{'接口版本: 2.5'},{'厂商ID: 0099'},{'MSGID: UUID'},{'违法数据来源: 9'},{'号牌种类：附录'},{'号牌号码: 识别到的号牌'},{'采集时间: YYYY-MM-DD HH:MM:SS'},{'违法代码: 参考公安标准'},{'采集点编号: 参考'},{'采集地址: 地址'},{'采集机关代码: 12位'},{'数据来源: 参考'},{'抓拍类型：1'},{'设备编号: 参考'},{'方向编号: 参考'},{'证据图片1：图片URL'},{'证据图片2：图片URL'},{'证据图片3：图片URL'},{'执勤民警：警号'},{'触发决定书编号：15位'},{'视频证据：URL-5秒视频'},{'号牌特征信息：附录'},{'号牌颜色：附录'},{'数据上传时间：YYYY-MM-DD HH：MM：SS'},{'是否已审：0'},{'车道编号：参考'}"
    illegal2 = ",".join([
        '接口类型: ILLEGAL04',
        '接口版本: 2.5',
        '厂商ID: 0099',
        'MSGID: UUID',
        '违法数据来源: 9',
        '号牌种类：99',
        '号牌号码: 川A00001',
        '采集时间: YYYY-MM-DD HH:MM:SS',
        '违法代码: 3001',
        '采集点编号: 620522000000',
        '采集地址: 甘肃省秦安县',
        '采集机关代码: 000000000000',
        '数据来源: 05',
        '抓拍类型：1',
        '设备编号: 620522000000050000',
        '方向编号: 0',
        '证据图片1：图片URL',
        '证据图片2：图片URL',
        '证据图片3：图片URL',
        '执勤民警：6205220000',
        '触发决定书编号：0123456789ABCDEF',
        '视频证据：URL-5秒视频',
        '号牌特征信息：819/1506/122/26/1',
        '号牌颜色：绿色',
        '数据上传时间：YYYY-MM-DD HH：MM：SS',
        '是否已审：0',
        '车道编号：参考'
    ])
    """
    ILLEGAL01,2.4,0002,7eca4af22a3711eeb8a1d5dfb59bd1ea,1,02,粤XXXXX,2023-07-24 15:32:44,1117,000011013000,XXXXX路口,440703000000,01,1,440703000000010448,1,02,,0,ftp://XX:XX@44.111.11.110:21/weifa/1/weifa/2023/07/24/15/2-20230724153244280-weifa-1117-(1).jpg,ftp://XX:XX@44.111.11.110:21/weifa/1/weifa/2023/07/24/15/2-20230724153245561-weifa-1117-(2).jpg,ftp://XX:XX@44.111.11.110:21/weifa/1/weifa/2023/07/24/15/2-20230724153340980-weifa-1117-(3).jpg,ftp://XX:XX@44.111.11.110:21/weifa/1/weifa/2023/07/24/15/2-20230724153245561-weifa-1117-(2).avi,2400/2067/168/46/1,2,2023-07-24 15:33:53,0
    """
    # print(illegal0)
    # print(illegal2)
    # print(illegal0 == illegal2)
    # send_to_topic(topic_illegal, illegal2)
    # receive_from_topic(topic_illegal)
    print(gps_xml)
