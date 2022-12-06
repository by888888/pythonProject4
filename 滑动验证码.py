from selenium import webdriver
import requests
import cv2 as cv2
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ChromeOptions  # 这个包用来规避被检测的风险
import time  # 延迟
from selenium.webdriver import ActionChains  # 动作链

option = webdriver.ChromeOptions()
option.add_experimental_option('useAutomationExtension', False)
option.add_experimental_option('excludeSwitches', ['enable-automation'])
driver_path = r'D:\chromedriver'  # 定义好路径
driver = webdriver.Chrome(executable_path=driver_path, options=option)  # 初始化路径+规避检测
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})
url = 'https://www.cnhnb.com/hangqing/cigu/'
driver.maximize_window()


def denglv():
    driver.get(url)
    time.sleep(4)
    # driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="anony-reg-new"]/div/div[1]/iframe'))  # 切入登录网址
    # dianjimimadenglv = driver.find_element_by_xpath('/html/body/div[1]/div[1]/ul[1]/li[2]').click()  # 点击账号密码登录
    # time.sleep(1)
    # zhanghao = driver.find_element_by_xpath('//input[@id="username"]').send_keys('ununun')  # 输入账号
    # time.sleep(1)
    # mima = driver.find_element_by_xpath('//input[@id="password"]').send_keys('7878787878')  # 输入密码
    # time.sleep(2)
    # denglv = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[5]/a').click()  # 点击登录
    # time.sleep(3)
    while True:
        tupian()
        x = jiexi()
        x = int(x * 282 / 680) - 22
        print(x)
        tracks = get_tracks(x)
        action = ActionChains(driver)
        # 按住滑块元素
        action.click_and_hold(ele_hk).perform()
        # 滑动
        for track in tracks:
            ActionChains(driver).move_by_offset(xoffset=track, yoffset=0).perform()
        ActionChains(driver).move_by_offset(xoffset=5, yoffset=0).perform()
        ActionChains(driver).move_by_offset(xoffset=-5, yoffset=0).perform()
        # 松开鼠标
        action.release(ele_hk).perform()
        try:
            time.sleep(3)
            refresh = driver.find_element_by_xpath('//div[@id="reload"]').click()  # 刷新按钮
        except Exception as e:
            break


def tupian():
    driver.switch_to_frame("tcaptcha_iframe")
    ele_bj = driver.find_element_by_xpath('//img[@id="slideBg"]')  # 背景图片
    global ele_hk
    ele_hk = driver.find_element_by_xpath('//img[@id="slideBlock"]')
    src_bj = ele_bj.get_attribute('src')  # 获取bj图片下载地址
    src_hk = ele_hk.get_attribute('src')  # 获取滑块图片下载地址
    # 用resqust下载图片
    content = requests.get(src_bj).content  # 下载背景
    f = open('bj.jpg', mode='wb')
    f.write(content)
    f.close()
    print('下载完成背景图片')
    time.sleep(1)
    content1 = requests.get(src_hk).content  # 下载滑块
    f = open('hk.jpg', mode='wb')
    f.write(content1)
    f.close()
    print('下载完成滑块图片')


def jiexi():
    bj_rgb = cv2.imread('bj.jpg')
    # 灰度处理
    bj_gray = cv2.cvtColor(bj_rgb, cv2.COLOR_BGR2GRAY)
    # 读取滑块的RGB
    hk_rgb = cv2.imread('hk.jpg', 0)
    # 匹配滑块在背景图的位置
    res = cv2.matchTemplate(bj_gray, hk_rgb, cv2.TM_CCOEFF_NORMED)
    # 获取位置
    location = cv2.minMaxLoc(res)
    print(location[2][0])
    return location[2][0]


def get_tracks(distance):
    # 初速度
    v = 0
    # 计算间隔
    t = 0.2
    tracks = []
    # 当前位移
    current = 0
    # 减速阈值
    while current < distance:
        # 加速度为正 2
        a = 2
        # 初速度 v0
        v0 = v
        # 当前速度 v = v0 + at
        v = v0 + a * t
        # 移动距离 x = v0t + 1/2 * a * t^2
        move = v0 * t + 0.5 * a * (t * t)
        # 当前位移
        current += move
        # 加入轨
        tracks.append(round(move))
        v = v0 + a * t
    return tracks


if __name__ == '__main__':
    denglv()