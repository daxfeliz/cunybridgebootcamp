# get_pkmn_color_pallete
Can't choose your favorite color palette? Choose your favorite pokemon! 

This code is depends on colortheif ( https://github.com/fengsp/color-thief-py ) which is easy to install via pip:

pip install colorthief

All you you need is to enter your favorite pokemon's name!

Example usage:

    #pkmn='mewtwo' 
    
    #pkmn='pikachu'
    
    #pkmn='pichu'

    #pkmn='Charizard'
    
    pkmn='calyrex'
    
    pkmn=str(413)
    
    colors = get_pkmn_pallete(pkmn)
    
    for x in range(len(colors)):
    
        plt.scatter(x,np.sin(x),color=np.array(colors[x]),s=20**2)
        
    plt.gca().set_facecolor('black')
    
    plt.xticks([])
    
    plt.yticks([])
    
    plt.savefig('pkmn_pallete.png')
    
    plt.show()


![pkmn_pallete.png](pkmn_pallete.png)
