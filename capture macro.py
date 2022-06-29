import pyautogui as auto
import time
import pyperclip

total_page = 836 #전체  페이지  설정
book_name = 'ebook' # 파일 이름 설정
capture_pos = (772, 269) # 캡처 위치 설정 
ebook_screen_center_pos = (471, 533) # 스크린 
right_pos=(1364,431) #키보드 우측 클릭 좌표
sleep_time = 1.0 # 지연시간

time.sleep(5.) # 5초 딜레이

for i in range(int(total_page/2)):
    file_name = book_name + '_' + str(i+1).zfill(4) + '.png'
    pyperclip .copy(file_name)

    auto.click(capture_pos)
    time.sleep(sleep_time)

    auto.hotkey('ctrl', 'v')
    time.sleep(sleep_time)

    auto.press('enter')
    time.sleep(sleep_time)

    auto.click(ebook_screen_center_pos) 
    time.sleep(sleep_time)

    auto.press('enter')
    time.sleep(sleep_time)
    
    auto.press('right')

    time.sleep(sleep_time)


    auto.click(right_pos) #자동 우측 클릭

    time.sleep(sleep_time)
    
    auto.press('enter')
    time.sleep(sleep_time)

    print(str(i+1), '/', int(total_page/2))