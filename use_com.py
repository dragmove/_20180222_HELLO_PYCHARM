# functions
def run():
    import win32com.client

    explore = win32com.client.Dispatch('InternetExplorer.Application')
    explore.Visible = True

    word = win32com.client.Dispatch('Word.Application')
    word.Visible = True

# implementation
if __name__ == '__main__':
    run()