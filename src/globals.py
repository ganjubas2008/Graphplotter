CANV_SZ = [300, 435]
SCROLLBAR_SZ = [102, 150]
BUTTON_SZ = [48, 188]

DEL_BUTTON_SZ = [58, -1]

CANV_X0 = SCROLLBAR_SZ[1]
CANV_X = [CANV_X0, CANV_X0 + CANV_SZ[1]]
CANV_Y0 = BUTTON_SZ[0]
CANV_Y = [CANV_Y0, CANV_Y0 + CANV_SZ[0]]

SCROLL_DELTA = 120
CANV_ACCURACY = 100
INF = 1e9

global_kwargs = {}

COLORS = [
    'dark slate gray',
    'dim gray',
    'slate gray',
    'light slate gray',
    'gray',
    'light grey',
    'midnight blue',
    'navy',
    'cornflower blue',
    'dark slate blue',
    'slate blue',
    'medium slate blue',
    'light slate blue',
    'medium blue',
    'royal blue',
    'blue',
    'dodger blue',
    'deep sky blue',
    'sky blue',
    'light sky blue',
    'steel blue',
    'light steel blue',
    'light blue',
    'powder blue',
    'pale turquoise',
    'dark turquoise',
    'medium turquoise',
    'turquoise',
    'cyan',
    'light cyan',
    'cadet blue',
    'medium aquamarine',
    'aquamarine',
    'dark green',
    'dark olive green',
    'dark sea green',
    'sea green',
    'medium sea green',
    'light sea green',
    'pale green',
    'spring green',
    'lawn green',
    'medium spring green',
    'green yellow',
    'lime green',
    'yellow green',
    'forest green',
    'olive drab',
    'dark khaki',
    'khaki',
    'pale goldenrod',
    'light goldenrod yellow',
    'light yellow',
    'yellow',
    'gold',
    'light goldenrod',
    'goldenrod',
    'dark goldenrod',
    'rosy brown',
    'indian red',
    'saddle brown',
    'sandy brown',
    'dark salmon',
    'salmon',
    'light salmon',
    'orange',
    'dark orange',
    'coral',
    'light coral',
    'tomato',
    'orange red',
    'red',
    'hot pink',
    'deep pink',
    'pink',
    'light pink',
    'pale violet red',
    'maroon',
    'medium violet red',
    'violet red',
    'SlateBlue1',
    'SlateBlue2',
    'SlateBlue3',
    'SlateBlue4',
    'RoyalBlue1',
    'RoyalBlue2',
    'RoyalBlue3',
    'RoyalBlue4',
    'blue2',
    'blue4',
    'DodgerBlue2',
    'DodgerBlue3',
    'DodgerBlue4',
    'SteelBlue1',
    'SteelBlue2',
    'SteelBlue3',
    'SteelBlue4',
    'DeepSkyBlue2',
    'DeepSkyBlue3',
    'DeepSkyBlue4',
    'CadetBlue4',
    'turquoise1',
    'turquoise2',
    'turquoise3',
    'turquoise4',
    'cyan2',
    'cyan3',
    'cyan4',
    'DarkSlateGray1',
    'DarkSlateGray2',
    'DarkSlateGray3',
    'DarkSlateGray4',
    'aquamarine2',
    'aquamarine4',
    'DarkSeaGreen1',
    'DarkSeaGreen2',
    'DarkSeaGreen3',
    'DarkSeaGreen4',
    'SeaGreen1',
    'SeaGreen2',
    'SeaGreen3',
    'PaleGreen1',
    'PaleGreen2',
    'PaleGreen3',
    'PaleGreen4',
    'SpringGreen2',
    'SpringGreen3',
    'SpringGreen4',
    'green2',
    'green3',
    'green4',
    'chartreuse2',
    'chartreuse3',
    'chartreuse4',
    'OliveDrab1',
    'OliveDrab2',
    'OliveDrab4',
    'DarkOliveGreen1',
    'DarkOliveGreen2',
    'DarkOliveGreen3',
    'DarkOliveGreen4',
    'khaki1',
    'khaki2',
    'khaki3',
    'khaki4',
    'LightGoldenrod1',
    'LightGoldenrod2',
    'LightGoldenrod3',
    'LightGoldenrod4',
    'yellow2',
    'yellow3',
    'yellow4',
    'gold2',
    'gold3',
    'gold4',
    'goldenrod1',
    'goldenrod2',
    'goldenrod3',
    'goldenrod4',
    'DarkGoldenrod1',
    'DarkGoldenrod2',
    'DarkGoldenrod3',
    'DarkGoldenrod4',
    'RosyBrown1',
    'RosyBrown2',
    'RosyBrown3',
    'RosyBrown4',
    'IndianRed1',
    'IndianRed2',
    'IndianRed3',
    'IndianRed4',
    'sienna1',
    'sienna2',
    'sienna3',
    'sienna4',
    'burlywood1',
    'burlywood2',
    'burlywood3',
    'burlywood4',
    'tan1',
    'tan2',
    'tan4',
    'chocolate1',
    'chocolate2',
    'chocolate3',
    'firebrick1',
    'firebrick2',
    'firebrick3',
    'firebrick4',
    'brown1',
    'brown2',
    'brown3',
    'brown4',
    'salmon1',
    'salmon2',
    'salmon3',
    'salmon4',
    'LightSalmon2',
    'LightSalmon3',
    'LightSalmon4',
    'orange2',
    'orange3',
    'orange4',
    'DarkOrange1',
    'DarkOrange2',
    'DarkOrange3',
    'DarkOrange4',
    'coral1',
    'coral2',
    'coral3',
    'coral4',
    'tomato2',
    'tomato3',
    'tomato4',
    'OrangeRed2',
    'OrangeRed3',
    'OrangeRed4',
    'red2',
    'red3',
    'red4',
    'DeepPink2',
    'DeepPink3',
    'DeepPink4',
    'HotPink1',
    'HotPink2',
    'HotPink3',
    'HotPink4',
    'pink3',
    'pink4',
    'LightPink1',
    'LightPink2',
    'LightPink3',
    'LightPink4',
    'PaleVioletRed1',
    'PaleVioletRed2',
    'PaleVioletRed3',
    'PaleVioletRed4',
    'maroon1',
    'maroon2',
    'maroon3',
    'maroon4',
    'VioletRed1',
    'VioletRed2',
    'VioletRed3',
    'VioletRed4',
    'magenta2',
    'magenta3',
    'magenta4',
    'orchid1',
    'orchid2',
    'orchid3',
    'orchid4',
    'MediumOrchid1',
    'MediumOrchid2',
    'MediumOrchid3',
    'MediumOrchid4',
    'DarkOrchid1',
    'DarkOrchid2',
    'DarkOrchid3',
    'DarkOrchid4',
    'purple1',
    'purple2',
    'purple3',
    'purple4',
    'MediumPurple1',
    'MediumPurple2',
    'MediumPurple3',
    'MediumPurple4',
    ]
