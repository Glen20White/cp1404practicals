import wikipedia

def main():
    while True:
        page_title_input = input("Enter page title: ")
        if page_title_input == "":
            print("Thank you")
            break

        try:
            page = wikipedia.page(page_title_input, auto_suggest=False)
            print(page.title)
            print(page.summary)
            print(page.url)

        except wikipedia.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:", e.options)
        except wikipedia.PageError as e:
            print(f"Page id '{page_title_input}' does not match any pages. Try another id!")

main()