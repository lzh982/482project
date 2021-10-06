from epicstore_api import EpicGamesStoreAPI
from datetime import datetime
import json



def main():

    presentiso = datetime.now()
    present = presentiso.strftime("%Y-%m-%d")
    print("Today's date: ", present)
    search = 'fort'
    print('executed')
    api = EpicGamesStoreAPI()
    
    slug_dict = api.get_product_mapping()
    
    games = api.fetch_store_games(
        product_type='games/edition/base|bundles/games|editors',
        count=3,
        sort_by='releaseDate',
        sort_dir='DESC',
        release_date="[,"+present+"]",
        keywords = search,
        with_price = True
    )['data']['Catalog']['searchStore']['elements']
    print()
    
    for game in games:
        game_name = game['title']
        game_thumbnail = None
        game_namespace = game['namespace']
        for image in game['keyImages']:
            if image['type'] == 'Thumbnail':
                game_thumbnail = image['url']
        
        game_oprice = game['price']['totalPrice']['fmtPrice']['originalPrice']
        game_dprice = game['price']['totalPrice']['fmtPrice']['discountPrice']
        game_dev = game['seller']['name']
        print("Name:", game_name)
        print("Price:", game_dprice)
        if game_namespace in slug_dict:
            game_slug = slug_dict[game_namespace]
        else:
            raise Exception("Slug not found")
        game_url = "https://www.epicgames.com/store/en-US/p/" + game_slug
            
    print()
    print("finished")
    print()
        

if __name__ == '__main__':
    main()