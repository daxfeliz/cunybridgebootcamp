def get_pkmn_pallete(pkmn_name):
    '''
    This function performs a URL request from the pokeapi.co website to grab
    a pokemon sprite from pokemon sprite artwork. The color palletes are then
    extracted using Color Theif to produce 8 color outputs as a numpy array.

    Input: int or str, national pokedex number or pokemon name (no typos!)

    Returns: np.ndarray, 8 colors from the input pokemon's color pallete. 

    '''
    import numpy as np
    from urllib.request import Request, urlopen
    import urllib
    import io
    from colorthief import ColorThief
    
    #check if pokedex ID or pokemon name is input
    if pkmn_name.isnumeric()==True:
        import requests
        import json
        #need to get pokemon name, let's use https://pokeapi.co/
        url = ('http://pokeapi.co/api/v2/pokemon/' + pkmn_name ) # URL from pokeapi.co using pokemon list API
        r = requests.get(url)
        pokedex_data = json.loads(r.text)
        pkmn_name = pokedex_data[u'name']
    
    #check for upper case spelling, must be lowercase
    if pkmn_name[0].isupper()==True:
        pkmn_name=pkmn_name.lower()
    print('getting',pkmn_name,'sprite colors!')
    sprite_url = 'https://img.pokemondb.net/artwork/large/'+str(pkmn_name)+'.jpg'

#     fd = urlopen(sprite_url)
    req = Request(sprite_url, headers={'User-Agent': 'Mozilla/5.0'})
    fd = urlopen(req).read()
    #
    f = io.BytesIO(fd)
    color_thief = ColorThief(f)
    #
    # print(color_thief.get_color(quality=1))
    # print(color_thief.get_palette(quality=1))
    #
    #divide by 255 to get RGB ranging from 0-1
    return np.array(color_thief.get_palette(quality=1))/255
