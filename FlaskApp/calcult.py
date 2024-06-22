import matplotlib.pyplot as plt
import io
import base64

def create_plot():
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 16, 25]
    plt.figure(facecolor='#f4f4f4' )
    plt.plot(x, y)
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf-8')
    return plot_url



