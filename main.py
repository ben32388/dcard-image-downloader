import requests
import os

def get_image_urls(post_id):
    res = requests.get(f'https://www.dcard.tw/_api/posts/{post_id}')
    data = res.json()
    return [d.get('url','') for d in data.get('media', [])], res.status_code

def download_image(url, folder_name):
    res = requests.get(url, stream=True)
    filename = url.split('/')[-1]
    # wb用二進位寫入
    with open(os.path.join(folder_name, filename), 'wb') as f:
        for chunk in res:
            f.write(chunk)   


def main():
    post_id = input('Post ID: ')
    urls, status_code = get_image_urls(post_id)
    # print('\n'.join(urls))
    if status_code != 200:
        print("Not found.")
        return
    for i, url in enumerate(urls, 1):
        message = '[{}/{}] {}'.format(i, len(urls), '#' * i)
        print(message, end='\r')
        folder_name = f'post_{post_id}'
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        download_image(url, folder_name)
    print('\nFinish')

# 是主要程式執行的時候才用，當成套件import時不會
if __name__ == '__main__':
    main()



# res = requests.get('https://www.dcard.tw/_api/posts/232241665')
# media = res.json()['media']

# for m in media:
#     print(m['url'])

# for k, v in res.json().items():
#     if(k =="media"):
#         for a in v:
#          print(a['url'])
# 終極密碼
# 幾A幾B
        
    