import csv
import requests
from bs4 import BeautifulSoup
import re
p = ['/hangqing/zidxm/', '/hangqing/caigua/', '/hangqing/xuetc/', '/hangqing/cdlist-2003192-0-23-0-0-1/', '/hangqing/fugc/', '/hangqing/lusun/', '/hangqing/nwc/', '/hangqing/pinggu/', '/hangqing/xyumi/', '/hangqing/huzj/', '/hangqing/shuhc/', '/hangqing/cdlist-2003192-0-29-0-0-1/', '/hangqing/honggua/', '/hangqing/huajy/', '/hangqing/maodou/', '/hangqing/yanghe/', '/hangqing/sld/', '/hangqing/gouzd/', '/hangqing/husj/', '/hangqing/bingcao/', '/hangqing/xianc/', '/hangqing/fengweig/', '/hangqing/taocai/', '/hangqing/cdlist-2003192-0-45081-0-0-1/', '/hangqing/helg/', '/hangqing/lujiaoc/', '/hangqing/hung/', '/hangqing/tuershao/', '/hangqing/nuomishu/', '/hangqing/kuzc/', '/hangqing/xianqs/', '/hangqing/jicai/', '/hangqing/yangdj/', '/hangqing/bans/', '/hangqing/nanjiang/', '/hangqing/doubanc/', '/hangqing/liuhy/', '/hangqing/cyyxh/', '/hangqing/wosun/', '/hangqing/sxiangc/', '/hangqing/siguajian/', '/hangqing/huanzg/', '/hangqing/songm/', '/hangqing/maos/', '/hangqing/slc/', '/hangqing/renshencai/', '/hangqing/zhuy/', '/hangqing/lurg/', '/hangqing/songly/', '/hangqing/zsb/', '/hangqing/hsh/', '/hangqing/dasuan/', '/hangqing/liudingg/', '/hangqing/fanxing/', '/hangqing/jizj/', '/hangqing/ssc/', '/hangqing/huoliancai/', '/hangqing/cdlist-2003192-0-5-0-0-1/', '/hangqing/cdlist-2003192-0-19-0-0-1/', '/hangqing/songsj/', '/hangqing/guangyu/', '/hangqing/baicj/', '/hangqing/jisongrong/', '/hangqing/cdlist-2003192-0-16-0-0-1/', '/hangqing/syec/', '/hangqing/genqin/', '/hangqing/shengjiang/', '/hangqing/shanyd/', '/hangqing/changsc/', '/hangqing/hhcai/', '/hangqing/qiukui/', '/hangqing/xcy/', '/hangqing/tacai/', '/hangqing/edj/', '/hangqing/yangcong/', '/hangqing/cdlist-2003192-0-45086-0-0-1/', '/hangqing/xbg/', '/hangqing/yxc/', '/hangqing/wandouo/', '/hangqing/zhemzc/', '/hangqing/yugeng/', '/hangqing/xiangrg/', '/hangqing/longzg/', '/hangqing/bc/', '/hangqing/naijj/', '/hangqing/jiecaitou/', '/hangqing/wumijun/', '/hangqing/cdlist-2003192-0-20-0-0-1/', '/hangqing/yuns/', '/hangqing/jinqh/', '/hangqing/xhs/', '/hangqing/lagen/', '/hangqing/ligu/', '/hangqing/hongshuye/', '/hangqing/shanlucai/', '/hangqing/zhenm/', '/hangqing/zhimy/', '/hangqing/xuelianguo/', '/hangqing/yeconghua/', '/hangqing/cdlist-2003192-0-7-0-0-1/', '/hangqing/fsgtj/', '/hangqing/sbg/', '/hangqing/sum/', '/hangqing/langcai/', '/hangqing/facai/', '/hangqing/yangji/', '/hangqing/nangua/', '/hangqing/htg/', '/hangqing/mzx/', '/hangqing/haixg/', '/hangqing/zhuj/', '/hangqing/xilt/', '/hangqing/cdlist-2003192-0-13-0-0-1/', '/hangqing/shuangbg/', '/hangqing/yinpg/', '/hangqing/qingmingcai/', '/hangqing/cdlist-2003192-0-24-0-0-1/', '/hangqing/shier/', '/hangqing/youky/', '/hangqing/shanyao/', '/hangqing/bajiaoh/', '/hangqing/xiamigu/', '/hangqing/cdlist-2003192-0-17-0-0-1/', '/hangqing/lajiao/', '/hangqing/cigu/', '/hangqing/baiyudou/', '/hangqing/xiangedy/', '/hangqing/kuth/', '/hangqing/hounaojun/', '/hangqing/cdlist-2003192-0-28-0-0-1/', '/hangqing/kuz/', '/hangqing/mlt/', '/hangqing/kxco/', '/hangqing/yelian/', '/hangqing/fengjiang/', '/hangqing/ngt/', '/hangqing/liangshu/', '/hangqing/hem/', '/hangqing/huihc/', '/hangqing/shanmz/', '/hangqing/shuijingcai/', '/hangqing/songrong/', '/hangqing/yangjiang/', '/hangqing/congtou/', '/hangqing/jiangshu/', '/hangqing/xiaojc/', '/hangqing/hualianmo/', '/hangqing/suantai/', '/hangqing/qinggj/', '/hangqing/congz/', '/hangqing/beicc/', '/hangqing/weic/', '/hangqing/saozc/', '/hangqing/shengcai/', '/hangqing/bibgj/', '/hangqing/jiuhuang/', '/hangqing/baishenjun/', '/hangqing/xiaomy/', '/hangqing/shanjiang/', '/hangqing/nendm/', '/hangqing/jielan/', '/hangqing/shaog/', '/hangqing/shanyc/', '/hangqing/mayecai/', '/hangqing/jiaotou/', '/hangqing/baoyugu/', '/hangqing/yuanm/', '/hangqing/sigua/', '/hangqing/bocai/', '/hangqing/jig/', '/hangqing/kuju/', '/hangqing/tudou/', '/hangqing/songrg/', '/hangqing/qingtj/', '/hangqing/huixt/', '/hangqing/xianggu/', '/hangqing/jiuch/', '/hangqing/cdlist-2003192-0-10-0-0-1/', '/hangqing/xiuzg/', '/hangqing/qiaomy/', '/hangqing/pucai/', '/hangqing/baocai/', '/hangqing/jitg/', '/hangqing/labaj/', '/hangqing/dpc/', '/hangqing/zhenzhc/', '/hangqing/songl/', '/hangqing/xlh/', '/hangqing/fsgg/', '/hangqing/maojg/', '/hangqing/hyc/', '/hangqing/bailg/', '/hangqing/yelh/', '/hangqing/cdlist-2003192-0-11-0-0-1/', '/hangqing/bygds/', '/hangqing/msangjun/', '/hangqing/cdlist-2003192-0-45085-0-0-1/', '/hangqing/dayq/', '/hangqing/cdlist-2003192-0-6-0-0-1/', '/hangqing/ercai/', '/hangqing/qincai/', '/hangqing/lianpeng/', '/hangqing/shanbeigu/', '/hangqing/cdlist-2003192-0-8-0-0-1/', '/hangqing/sangy/', '/hangqing/mabogu/', '/hangqing/jiut/', '/hangqing/pancai/', '/hangqing/longh/', '/hangqing/shanyucai/', '/hangqing/cdlist-2003192-0-4-0-0-1/', '/hangqing/cdlist-2003192-0-18-0-0-1/', '/hangqing/shuzc/', '/hangqing/hld/', '/hangqing/mdx/', '/hangqing/cdlist-2003192-0-21-0-0-1/', '/hangqing/luobo/', '/hangqing/gunc/', '/hangqing/qiezi/', '/hangqing/maty/', '/hangqing/yulancai/', '/hangqing/mec/', '/hangqing/niushejun/', '/hangqing/donggua/', '/hangqing/chouc/', '/hangqing/huolongguoh/', '/hangqing/lingzhigu/', '/hangqing/shacong/', '/hangqing/yuer/', '/hangqing/gegen/', '/hangqing/xmc/', '/hangqing/youdj/', '/hangqing/yinsc/', '/hangqing/sijidou/', '/hangqing/jiucai/', '/hangqing/mulanya/', '/hangqing/lecai/', '/hangqing/mushu/', '/hangqing/lbc/', '/hangqing/ningmy/', '/hangqing/xxcd/', '/hangqing/xbh/', '/hangqing/wawacai/', '/hangqing/suanh/', '/hangqing/jxc/', '/hangqing/dongsun/', '/hangqing/hongqiujiang/', '/hangqing/liuxm/', '/hangqing/maozz/', '/hangqing/gouqy/', '/hangqing/jiansq/', '/hangqing/xinxblg/', '/hangqing/cdlist-2003192-0-3-0-0-1/', '/hangqing/luoby/', '/hangqing/longbaiya/', '/hangqing/musuya/', '/hangqing/yde/', '/hangqing/miantc/', '/hangqing/lingjiao/', '/hangqing/chuncai/', '/hangqing/cly/', '/hangqing/yinkj/', '/hangqing/qiny/', '/hangqing/dacong/', '/hangqing/qiansg/', '/hangqing/shajiang/', '/hangqing/zis/', '/hangqing/xiangc/', '/hangqing/zisu/', '/hangqing/xbc/', '/hangqing/tonghao/', '/hangqing/lizj/', '/hangqing/yesuan/', '/hangqing/mogu/', '/hangqing/ymc/', '/hangqing/kucai/', '/hangqing/cdlist-2003192-0-45083-0-0-1/', '/hangqing/zhimc/', '/hangqing/tianqic/', '/hangqing/kugua/', '/hangqing/haohc/', '/hangqing/cdlist-2003192-0-15-0-0-1/', '/hangqing/cdlist-2003192-0-27-0-0-1/', '/hangqing/zihj/', '/hangqing/jianpengcao/', '/hangqing/shangc/', '/hangqing/jsjg/', '/hangqing/suanmiao/', '/hangqing/cdlist-2003192-0-26-0-0-1/', '/hangqing/kuly/', '/hangqing/xiangcai/', '/hangqing/hongshu/', '/hangqing/ganbj/', '/hangqing/dlh/', '/hangqing/jiaobai/', '/hangqing/gecong/', '/hangqing/zhisr/', '/hangqing/cdlist-2003192-0-45084-0-0-1/', '/hangqing/fsg/', '/hangqing/xiongzhanggu/', '/hangqing/poudai/', '/hangqing/kuyc/', '/hangqing/quqc/', '/hangqing/xqj/', '/hangqing/dugua/', '/hangqing/kucihua/', '/hangqing/huangxc/', '/hangqing/lamucai/', '/hangqing/houtc/', '/hangqing/moy/', '/hangqing/heym/', '/hangqing/cdlist-2003192-0-12-0-0-1/', '/hangqing/yuqian/', '/hangqing/ciqin/', '/hangqing/qingh/', '/hangqing/jiecaio/', '/hangqing/ciwujiacai/', '/hangqing/biandou/', '/hangqing/yuya/', '/hangqing/牛皮菜/', '/hangqing/douya/', '/hangqing/csg/', '/hangqing/maanjun/', '/hangqing/bah/', '/hangqing/hongg/', '/hangqing/jhc/', '/hangqing/huangjg/', '/hangqing/xingcai/', '/hangqing/caogu/', '/hangqing/shegua/', '/hangqing/chunc/', '/hangqing/xhl/', '/hangqing/tiancaitou/', '/hangqing/shuqiujun/', '/hangqing/ngj/', '/hangqing/yexiancai/', '/hangqing/mihuanjun/', '/hangqing/huasy/', '/hangqing/hetaoh/', '/hangqing/zhusun/', '/hangqing/laortj/', '/hangqing/yintiao/', '/hangqing/lianou/', '/hangqing/cdlist-2003192-0-14-0-0-1/', '/hangqing/bopigu/', '/hangqing/baiyugu/', '/hangqing/shanhlb/', '/hangqing/hlb/', '/hangqing/zhudg/', '/hangqing/dagqg/', '/hangqing/shc/', '/hangqing/yutou/', '/hangqing/xianggujiao/', '/hangqing/muer/', '/hangqing/xiaocong/', '/hangqing/tanglh/', '/hangqing/pugy/', '/hangqing/cdlist-2003192-0-31-0-0-1/', '/hangqing/cdlist-2003192-0-25-0-0-1/', '/hangqing/btc/', '/hangqing/jiyj/', '/hangqing/shanhj/', '/hangqing/cdlist-2003192-0-30-0-0-1/', '/hangqing/juecai/', '/hangqing/juju/', '/hangqing/shasongjian/', '/hangqing/lihao/', '/hangqing/diaoc/', '/hangqing/caitai/', '/hangqing/szcg/', '/hangqing/qingtoj/', '/hangqing/jzg/', '/hangqing/cdlist-2003192-0-45082-0-0-1/', '/hangqing/kuws/', '/hangqing/dipu/', '/hangqing/huangyg/', '/hangqing/cdlist-2003192-0-45114-0-0-1/', '/hangqing/yumsun/', '/hangqing/dongfc/', '/hangqing/huixiang/', '/hangqing/xueyingzi/', '/hangqing/tiancaimiao/', '/hangqing/liuhuangjun/', '/hangqing/huangguahua/', '/hangqing/xyac/', '/hangqing/hutai/', '/hangqing/huanggua/', '/hangqing/zbtk/', '/hangqing/daodou/', '/hangqing/luol/', '/hangqing/kuzhuguo/', '/hangqing/zishu/', '/hangqing/xuelianggu/', '/hangqing/donghancai/', '/hangqing/gongcai/', '/hangqing/liuhuacai/', '/hangqing/pielan/', '/hangqing/zihg/', '/hangqing/doujiao/', '/hangqing/wdm/', '/hangqing/nanguahua/', '/hangqing/shanmzc/', '/hangqing/yiner/', '/hangqing/goussui/', '/hangqing/cdlist-2003192-0-45087-0-0-1/', '/hangqing/xieweigu/', '/hangqing/hugua/', '/hangqing/hulu/', '/hangqing/yeqc/']
m = []
for i in range(len(p)):
    if '-' in p[i]:
        m.append(i)
p = [p[i] for i in range(len(p)) if (i not in m)]
# print(p)
url_lst1 = list(set(p))
# print(url_lst1)
output = open('222.csv', 'a+', newline='')
writer = csv.writer(output)
for row in url_lst1:
    if row:  # 去除空行
        writer.writerow([row])
print("保存文件成功，处理结束")