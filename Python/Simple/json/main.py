import json
import os.path


class PersonalLibeary:
    
    JSON_FILES = 'books.json'
    
    def __init__(self):
        super().__init__()
    
    def check_json_file(self):
        
        if os.path.isfile(self.JSON_FILES):
            return "File Exists!"
        else:
            with open(self.JSON_FILES, 'a') as file:
                file.close()
                return "File Created!"
    
    def add_book(self, title: str, author: str, publish_date: int, genre: str, status_read: bool):
        self.check_json_file()
        
        try:         
            with open(self.JSON_FILES, 'r', encoding='utf-8') as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    data = []
                
            new_book = {
                "title": title,
                "author": author,
                "publish_date": publish_date,
                "genre": genre,
                "status_read": status_read
            }
            
            data.append(new_book)

            with open(self.JSON_FILES, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=2, ensure_ascii=False)
                                    
                return "book added!"
        except Exception as e:
            return f"Erorr: {e}"

    
    def list_book(self):
        
        pass
            
    
    def search_book(self, title, author, genre):
        
        pass
    
    def change_status_read(self, title, status_read):
        
        pass
    
    def delete_book(self, title):
        
        pass
    
    def statistics(self):
        
        pass
    
book = PersonalLibeary()

print(book.add_book('tw', 'tw', 'tw', 'tw', 'tw'))