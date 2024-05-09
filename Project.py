import tkinter
import tkinter.messagebox
import tkinter.ttk
import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt


def currency_exchange():
    """Extract the amount written on the label number_1 and create a string that will later be used in dataframe"""
    """If the user writes anything other than a number an error will appear telling the user to input only numbers"""
    global number_1, quant

    try:
        enter_1 = float(number_1.get())

        quant = [enter_1]

        tkinter.messagebox.showinfo("Complete", "The currency exchange transaction was stored in Forex_Trading.csv.")
    except ValueError:
        tkinter.messagebox.showerror("Error", "Sorry, the report could not be written. Check that only numeric values "
                                              "are entered/Do not write anything on dropbox.")

    global currency_box
    """Download Adj close currency exchange from Yahoo Finance over 17 years. The program will print all of the data"""
    """Calculate the average of the adj close from the 17 years worth of data."""
    """Download the adj close currency exchange from the last recorded exchange rate (1 minute). The program will print the data"""
    """The quantity of US Dollars written on the program will be multiplied by both historical and current exchange rate"""
    if currency_box.get() == "MXN":
        mxn1 = yf.download(['MXN=X'], start='2005-01-01', end='2022-12-01')
        mxn_ret = mxn1['Adj Close']
        print(mxn_ret.to_string())
        mxn_hist = float(np.average(mxn_ret))
        mxn2 = yf.download(tickers='MXN=X', period='1m')
        mxn2_ret = mxn2['Adj Close']
        print(mxn2_ret.to_string())
        total_hist = float(np.multiply(mxn_hist, quant))
        total_curr = float(np.multiply(mxn2_ret, quant))
        """Create a dataframe that will turn into a csv file with the quantity written, exchange rates, and total from transaction."""
        """If the exchange rate from Historical exchange rate is more than current exchange rate currency is undervalued"""
        """If the exchange rate from Historical exchange rate is less than current exchange rate currency is overvalued"""
        """A messagebox will appear depending on both exchange rates mentioning if the currency is over or undervalued"""
        """The transaction totals from both exchange rates make it easy to see how much profit could be made"""
        data = {'Currency': "MXN",
                'Quantity': quant,
                'Historical Exchange': mxn_hist,
                'Current Exchange': mxn2_ret,
                'Total Historical': total_hist,
                'Total Current': total_curr
                }
        df = pd.DataFrame(data)
        df.to_csv('Forex_Trading.csv', index=False)
        if df['Historical Exchange'].to_string() >= df['Current Exchange'].to_string():
            tkinter.messagebox.showinfo("Buy Mexican Pesos!", "Based on Historical data (review Forex_Trading.csv) The "
                                                              "Mexican Peso is currently undervalued and should be "
                                                              "bought")
        else:
            tkinter.messagebox.showinfo("Sell Mexican Pesos!", "Based on Historical data (review Forex_Trading.csv) "
                                                               "The Mexican Peso is currently overvalued and should "
                                                               "be sold")
        """Create a plot showing the currency's exchange rate over time. And the current exchange rate"""
        """Plot will print at the end of the program """
        plt.title("Mexican Peso Exchange Rate over 17 years")
        plt.plot(mxn_ret, 'b.-', label='Historical Mexican Peso')
        plt.plot(mxn2_ret, 'g.-', label='Current Mexican Peso')
        plt.xlabel('Years')
        plt.ylabel('USD / MXN')
        plt.legend()
        mxn_ret.plot.line()
        plt.savefig('MXN_Trade_Figure.png', dpi=400)
        plt.show()

    elif currency_box.get() == "CAD":
        """The same process runs for the six remaining currencies"""
        cad1 = yf.download(['CAD=X'], start='2005-01-01', end='2022-12-01')
        cad_ret = cad1['Adj Close']
        print(cad_ret.to_string())
        cad_hist = float(np.average(cad_ret))
        cad2 = yf.download(tickers='CAD=X', period='1m')
        cad2_ret = cad2['Adj Close']
        print(cad2_ret.to_string())
        total_hist = float(np.multiply(cad_hist, quant))
        total_curr = float(np.multiply(cad2_ret, quant))

        data = {'Currency': "CAD",
                'Quantity': quant,
                'Historical Exchange': cad_hist,
                'Current Exchange': cad2_ret,
                'Total Historical': total_hist,
                'Total Current': total_curr
                }
        df = pd.DataFrame(data)
        df.to_csv('Forex_Trading.csv', index=False)
        if df['Historical Exchange'].to_string() >= df['Current Exchange'].to_string():
            tkinter.messagebox.showinfo("Buy Canadian Dollars!", "Based on Historical data (review Forex_Trading.csv) "
                                                                 "The Canadian Dollar is currently undervalued and "
                                                                 "should be bought")
        else:
            tkinter.messagebox.showinfo("Sell Canadian Dollars!", "Based on Historical data (review Forex_Trading.csv) "
                                                                  "The Canadian Dollar is currently overvalued and "
                                                                  "should be sold")
        plt.title("Canadian Dollar Exchange Rate over 17 years")
        plt.plot(cad_ret, 'b.-', label='Historical Canadian Dollar')
        plt.plot(cad2_ret, 'g.-', label='Current Canadian Dollar')
        plt.xlabel('Years')
        plt.ylabel('USD / CAD')
        plt.legend()
        cad_ret.plot.line()
        plt.savefig('CAD_Trade_Figure.png', dpi=400)
        plt.show()

    elif currency_box.get() == "AUD":
        aud1 = yf.download(['AUD=X'], start='2005-01-01', end='2022-12-01')
        aud_ret = aud1['Adj Close']
        print(aud_ret.to_string())
        aud_hist = float(np.average(aud_ret))
        aud2 = yf.download(tickers='AUD=X', period='1m')
        aud2_ret = aud2['Adj Close']
        print(aud2_ret.to_string())
        total_hist = float(np.multiply(aud_hist, quant))
        total_curr = float(np.multiply(aud2_ret, quant))

        data = {'Currency': "AUD",
                'Quantity': quant,
                'Historical Exchange': aud_hist,
                'Current Exchange': aud2_ret,
                'Total Historical': total_hist,
                'Total Current': total_curr
                }
        df = pd.DataFrame(data)
        df.to_csv('Forex_Trading.csv', index=False)
        if df['Historical Exchange'].to_string() >= df['Current Exchange'].to_string():
            tkinter.messagebox.showinfo("Buy Australian Dollars!", "Based on Historical data "
                                                                   "(review Forex_Trading.csv)"
                                                                   "The Australian Dollar is currently undervalued and"
                                                                   "should be bought")
        else:
            tkinter.messagebox.showinfo("Sell Australian Dollars!", "Based on Historical data (review "
                                                                    "Forex_Trading.csv) "
                                                                    "The Australian Dollar is currently overvalued and "
                                                                    "should be sold")
        plt.title("Australian Dollar Exchange Rate over 17 years")
        plt.plot(aud_ret, 'b.-', label='Historical Australian Dollar')
        plt.plot(aud2_ret, 'g.-', label='Current Australian Dollars')
        plt.xlabel('Years')
        plt.ylabel('USD / AUD')
        plt.legend()
        aud_ret.plot.line()
        plt.savefig('CAD_Trade_Figure.png', dpi=400)
        plt.show()

    elif currency_box.get() == "JPY":
        jpy1 = yf.download(['JPY=X'], start='2024-02-01', end='2024-03-27')
        jpy_ret = jpy1['Adj Close']
        print(jpy_ret.to_string())
        jpy_hist = float(np.average(jpy_ret))
        jpy2 = yf.download(tickers='JPY=X', period='1m')
        jpy2_ret = jpy2['Adj Close']
        print(jpy2_ret.to_string())
        total_hist = float(np.multiply(jpy_hist, quant))
        total_curr = float(np.multiply(jpy2_ret, quant))

        data = {'Currency': "JPY",
                'Quantity': quant,
                'Historical Exchange': jpy_hist,
                'Current Exchange': jpy2_ret,
                'Total Historical': total_hist,
                'Total Current': total_curr
                }
        df = pd.DataFrame(data)
        df.to_csv('Forex_Trading.csv', index=False)
        if df['Historical Exchange'].to_string() >= df['Current Exchange'].to_string():
            tkinter.messagebox.showinfo("Buy Japanese Yen!",
                                        "Based on Historical data (review Forex_Trading.csv) The "
                                        "Japanese Yen is currently undervalued and should be "
                                        "bought")
        else:
            tkinter.messagebox.showinfo("Sell Japanese Yen!",
                                        "Based on Historical data (review Forex_Trading.csv) "
                                        "The Japanese Yen is currently overvalued and should "
                                        "be sold")
        plt.title("Japanese Yen Exchange Rate over 17 years")
        plt.plot(jpy_ret, 'b.-', label='Historical Japanese Yen')
        plt.plot(jpy2_ret, 'g.-', label='Current Japanese Yen')
        plt.xlabel('Years')
        plt.ylabel('USD / JPY')
        plt.legend()
        jpy_ret.plot.line()
        plt.savefig('JPY_Trade_Figure.png', dpi=400)
        plt.show()

    elif currency_box.get() == "CHF":
        chf1 = yf.download(['CHF=X'], start='2005-01-01', end='2022-12-01')
        chf_ret = chf1['Adj Close']
        print(chf_ret.to_string())
        chf_hist = float(np.average(chf_ret))
        chf2 = yf.download(tickers='CHF=X', period='1m')
        chf2_ret = chf2['Adj Close']
        print(chf2_ret.to_string())
        total_hist = float(np.multiply(chf_hist, quant))
        total_curr = float(np.multiply(chf2_ret, quant))

        data = {'Currency': "CHF",
                'Quantity': quant,
                'Historical Exchange': chf_hist,
                'Current Exchange': chf2_ret,
                'Total Historical': total_hist,
                'Total Current': total_curr
                }
        df = pd.DataFrame(data)
        df.to_csv('Forex_Trading.csv', index=False)
        if df['Historical Exchange'].to_string() >= df['Current Exchange'].to_string():
            tkinter.messagebox.showinfo("Buy Swiss Franc!",
                                        "Based on Historical data (review Forex_Trading.csv) The "
                                        "Swiss Franc is currently undervalued and should be "
                                        "bought")
        else:
            tkinter.messagebox.showinfo("Sell Swiss Franc!",
                                        "Based on Historical data (review Forex_Trading.csv) "
                                        "The Swiss Franc is currently overvalued and should "
                                        "be sold")
        plt.title("Swiss Franc Exchange Rate over 17 years")
        plt.plot(chf_ret, 'b.-', label='Historical Swiss Franc')
        plt.plot(chf2_ret, 'g.-', label='Current Swiss Franc')
        plt.xlabel('Years')
        plt.ylabel('USD / CHF')
        plt.legend()
        chf_ret.plot.line()
        plt.savefig('CHF_Trade_Figure.png', dpi=400)
        plt.show()

    elif currency_box.get() == "EUR":
        eur1 = yf.download(['EUR=X'], start='2005-01-01', end='2022-12-01')
        eur_ret = eur1['Adj Close']
        print(eur_ret.to_string())
        eur_hist = float(np.average(eur_ret))
        eur2 = yf.download(tickers='EUR=X', period='1m')
        eur2_ret = eur2['Adj Close']
        print(eur2_ret.to_string())
        total_hist = float(np.multiply(eur_hist, quant))
        total_curr = float(np.multiply(eur2_ret, quant))

        data = {'Currency': "EUR",
                'Quantity': quant,
                'Historical Exchange': eur_hist,
                'Current Exchange': eur2_ret,
                'Total Historical': total_hist,
                'Total Current': total_curr
                }
        df = pd.DataFrame(data)
        df.to_csv('Forex_Trading.csv', index=False)
        if df['Historical Exchange'].to_string() >= df['Current Exchange'].to_string():
            tkinter.messagebox.showinfo("Buy Euro!",
                                        "Based on Historical data (review Forex_Trading.csv) The "
                                        "Euro is currently undervalued and should be "
                                        "bought")
        else:
            tkinter.messagebox.showinfo("Sell Euro!",
                                        "Based on Historical data (review Forex_Trading.csv) "
                                        "The Euro is currently overvalued and should "
                                        "be sold")
        plt.title("Euro Exchange Rate over 17 years")
        plt.plot(eur_ret, 'b.-', label='Historical Euro')
        plt.plot(eur2_ret, 'g.-', label='Current Euro')
        plt.xlabel('Years')
        plt.ylabel('USD / EUR')
        plt.legend()
        eur_ret.plot.line()
        plt.savefig('EUR_Trade_Figure.png', dpi=400)
        plt.show()

    elif currency_box.get() == "GBP":
        gbp1 = yf.download(['GBP=X'], start='2005-01-01', end='2022-12-01')
        gbp_ret = gbp1['Adj Close']
        print(gbp_ret.to_string())
        gbp_hist = float(np.average(gbp_ret))
        gbp2 = yf.download(tickers='GBP=X', period='1m')
        gbp2_ret = gbp2['Adj Close']
        print(gbp2_ret.to_string())
        total_hist = float(np.multiply(gbp_hist, quant))
        total_curr = float(np.multiply(gbp2_ret, quant))

        data = {'Currency': "GBP",
                'Quantity': quant,
                'Historical Exchange': gbp_hist,
                'Current Exchange': gbp2_ret,
                'Total Historical': total_hist,
                'Total Current': total_curr
                }
        df = pd.DataFrame(data)
        df.to_csv('Forex_Trading.csv', index=False)
        if df['Historical Exchange'].to_string() >= df['Current Exchange'].to_string():
            tkinter.messagebox.showinfo("Buy Pound sterling!",
                                        "Based on Historical data (review Forex_Trading.csv) The "
                                        "Pound sterling is currently undervalued and should be "
                                        "bought")
        else:
            tkinter.messagebox.showinfo("Sell Pound sterling!",
                                        "Based on Historical data (review Forex_Trading.csv) "
                                        "The Pound sterling is currently overvalued and should "
                                        "be sold")
        plt.title("Pound sterling Exchange Rate over 17 years")
        plt.plot(gbp_ret, 'b.-', label='Historical Pound sterling')
        plt.plot(gbp2_ret, 'g.-', label='Current Pound sterling')
        plt.xlabel('Years')
        plt.ylabel('USD / GBP')
        plt.legend()
        gbp_ret.plot.line()
        plt.savefig('GBP_Trade_Figure.png', dpi=400)
        plt.show()


def close_convertor():
    print("Have a nice day!")
    root.destroy()


root = tkinter.Tk()
root.title("Forex Exchange Convertor.")
root.configure(bg="pink")

label_1 = tkinter.Label(root, text="Choose currency:")
label_1.configure(bg="pink")
label_1.grid(row=0, column=0)

currency_box = tkinter.ttk.Combobox(root, values=["MXN", "CAD", "AUD", "JPY", "CHF", "EUR", "GBP"])
currency_box.current(0)
currency_box.grid(row=0, column=1)

label_2 = tkinter.Label(root, text="Input USD amount:")
label_2.configure(bg="pink")
label_2.grid(row=2, column=0)

number_1 = tkinter.Entry(root, width=7)
number_1.grid(row=2, column=1)

convert_button = tkinter.Button(root, text="Exchange Currency", command=currency_exchange)
convert_button.grid(row=0, column=2, padx=5, pady=5)
convert_button.configure(bg="pale green")

close_button = tkinter.Button(root, text="Close Converter", command=close_convertor)
close_button.grid(row=2, column=2, padx=5, pady=5)
close_button.configure(bg="dark orange")

root.mainloop()
