import wikipedia

def main():
    while True:
        page_title_input = input("Enter page title: ")
        page = wikipedia.page(page_title_input)
        print(page.title)
        print(page.summary)
        print(page.url)

main()