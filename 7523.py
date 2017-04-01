import matplotlib as mpl
import matplotlib.pyplot as plt

def two_2line_texts(x1, y1, spacing1, x2, y2, spacing2): 

    text_string = 'line1\nline2'
    plt.text(x1, y1, text_string, linespacing = spacing1, alpha = 0.5)
    plt.text(x2, y2, text_string, linespacing = spacing2, alpha = 0.5)
    plt.show()

# fig 1: 
two_2line_texts(x1 = .5, y1 = .5, spacing1 = 2, 
                x2 = .5, y2 = .5, spacing2 = 0.4) 

# fig 2: 
two_2line_texts(x1 = .5, y1 = .5, spacing1 = 0.4, 
                x2 = .5, y2 = .5, spacing2 = 2) 

# fig 3: 
two_2line_texts(x1 = .5, y1 = .5000000001, spacing1 = 0.4, 
                x2 = .5, y2 = .5, spacing2 = 2) 
