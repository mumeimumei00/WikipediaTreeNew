import wikipedia as wk
class retrieve:
    def __init__(self, item = "Quantum Physics"):
        self.item = item
        self.wp = wk.WikipediaPage(item)

    # print a list of search results
    def search(self):
        results = wk.search(self.item)
        for result in results:
            print("- " + result)

    def content(self):
        result = wk.WikipediaPage(self.item).content
        print(result)
    
    def references(self):
        result = wk.WikipediaPage(self.item).references
        print(result)

    def sections(self):
        result = wk.WikipediaPage(self.item).sections
        print(result)

    def links(self):
        result = wk.WikipediaPage(self.item).links
        result.sort(reverse = True, key =len)
        return result
    def linksposition(self):
   
        list_links = self.links()
        summary = self.wp.summary
        for word in list_links:
            print(word)
            summary = summary.replace(word, "")
        print(summary)
print(retrieve().links())
# retrieve().search()
# print(retrieve("Quantum Mechanics").links())
