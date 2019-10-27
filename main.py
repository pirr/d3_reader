from lib.getter import get_data, HTMLFilter


if __name__ == "__main__":
    print(r'''
_________/\\\______/\\\\\\\\\\____________________________________        
 ________\/\\\____/\\\///////\\\___________________________________       
  ________\/\\\___\///______/\\\____________________________________      
   ________\/\\\__________/\\\//__________/\\/\\\\\\\___/\\\____/\\\_     
    ___/\\\\\\\\\_________\////\\\________\/\\\/////\\\_\/\\\___\/\\\_    
     __/\\\////\\\____________\//\\\_______\/\\\___\///__\/\\\___\/\\\_   
      _\/\\\__\/\\\___/\\\______/\\\________\/\\\_________\/\\\___\/\\\_  
       _\//\\\\\\\/\\_\///\\\\\\\\\/____/\\\_\/\\\_________\//\\\\\\\\\__ 
        __\///////\//____\/////////_____\///__\///___________\/////////___
''')
    data = get_data()
    for post in data['posts']:
        print(post['title'])
        if post['data']['text']:
            parser = HTMLFilter()
            print(parser.feed(post['data']['text']))
            print(parser.text)
        if 'main_image_url' in post:
            print('image_url:', post['main_image_url'])
        print('rating:', post['rating'])
        print('link:', post['_links'][1]['href'])    
        print('=' * 25)