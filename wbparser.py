import os
import getpass
import sqlite3
import pandas as pd
import argparse


def parser_argument():
    parser = argparse.ArgumentParser(description='web browser parser') 

    parser.add_argument("--c", dest="chrome", action='store_true', help="chrome artifact")  
    parser.add_argument("--e", dest="edge", action='store_true', help="edge artifact")
    parser.add_argument("--f", dest="firefox", action='store_true', help="firefox artifacts") #store_true은 해당 인자가 입력되면 True 아니면 Fales 로 인식
    parser.add_argument("--a", dest="all", action='store_true', help="All Artifacts") 
    arge = parser.parse_args()
    
    username = getpass.getuser() # 경로
    path = os.path.join(f"C:/Users/{username}/Desktop/forensic_artifact")
    os.makedirs(path, exist_ok=True) 
    
    if os.path.isfile(f"C:/Users/{username}/AppData/Local/Google/Chrome/User Data/Default/History"):  
        p = os.path.join(f"C:/Users/{username}/AppData/Local/Google/Chrome/User Data/Default/History""")
        conn = sqlite3.connect(p)
        f = conn.cursor()  # 커서를 만들어줌

    
    if os.path.isfile(f"C:/Users/{username}/AppData/Local/Microsoft/Edge/User Data/Default/History"): 
        q = os.path.join(f"C:/Users/{username}/AppData/Local/Microsoft/Edge/User Data/Default/History""")
        conn = sqlite3.connect(q)
        s = conn.cursor()
        
    if os.path.isdir(f"C:/Users/{username}/AppData/Roaming/Mozilla/Firefox/Profiles"):
        uniq_dir = ''.join([file if ".default-release" in file else '' for file in os.listdir(f"C:/Users/{username}/AppData/Roaming/Mozilla/Firefox/Profiles/""")])   
        a = os.path.join(f"C:/Users/{username}/AppData/Roaming/Mozilla/Firefox/Profiles/{uniq_dir}/places.sqlite""")
        conn = sqlite3.connect(a)
        b = conn.cursor() 

    if arge.chrome:
        chromepath = os.path.join("C:/Users/",username,"Desktop/forensic_artifact/chrome_history/")
        os.makedirs(chromepath, exist_ok=True)
            
        f.execute("SELECT * FROM urls")
        cols = [column[0] for column in f.description] # 컬럼 가져옴
        datadf = pd.DataFrame.from_records(data=f.fetchall(), columns=cols)
        df = pd.DataFrame(datadf)
        df.to_csv(chromepath + "urls.csv")
            
        f.execute("SELECT * FROM `keyword_search_terms` ;")
        cols = [column[0] for column in f.description]
        datadf = pd.DataFrame.from_records(data=f.fetchall(), columns=cols)
        df = pd.DataFrame(datadf)
        df.to_csv(chromepath + "keyword_search_terms.csv")
        print(df)
            
        f.execute("SELECT * FROM `downloads` ;")
        cols = [column[0] for column in f.description]
        datadf = pd.DataFrame.from_records(data=f.fetchall(), columns=cols )
        conn.close()
        df = pd.DataFrame(datadf)
        df.to_csv(chromepath + "downloads.csv", sep='\t', escapechar='\b', header=False, index=False)
        print(df)
            
    elif arge.edge:
        
        edgepath = os.path.join(f"C:/Users/",username,"Desktop/forensic_artifact/edge_history/")
        os.makedirs(edgepath, exist_ok=True)
            
        s.execute("SELECT * FROM urls")
        cols = [column[0] for column in s.description] # 컬럼 가져옴
        datadf = pd.DataFrame.from_records(data=s.fetchall(), columns=cols)
        df = pd.DataFrame(datadf)
        df.to_csv(edgepath + "urls.csv")
            
        s.execute("SELECT * FROM `keyword_search_terms` ;")
        cols = [column[0] for column in s.description]
        datadf = pd.DataFrame.from_records(data=s.fetchall(), columns=cols)
        df = pd.DataFrame(datadf)
        df.to_csv(edgepath + "keyword_search_terms.csv")
        print(df)
            
        s.execute("SELECT * FROM `downloads` ;")
        cols = [column[0] for column in s.description]
        datadf = pd.DataFrame.from_records(data=s.fetchall(), columns=cols )
        conn.close()
        df = pd.DataFrame(datadf)
        df.to_csv(edgepath + "downloads.csv", sep='\t', escapechar='\b', header=False, index=False)
        print(df)
            
    elif arge.firefox:
        
        firefoxpath = os.path.join("C:/Users/",username,"Desktop/forensic_artifact/firefox_history/")
        os.makedirs(firefoxpath, exist_ok=True)
            
        b.execute("SELECT * FROM `moz_places` ;")
        cols = [column[0] for column in b.description] # 컬럼 가져옴
        datadf = pd.DataFrame.from_records(data=b.fetchall(), columns=cols)
        df = pd.DataFrame(datadf)
        df.to_csv(firefoxpath + "urls.csv")
            
            
        b.execute("SELECT * FROM `moz_bookmarks` ;")
        cols = [column[0] for column in b.description]
        datadf = pd.DataFrame.from_records(data=b.fetchall(), columns=cols)
        df = pd.DataFrame(datadf)
        df.to_csv(firefoxpath + "bookmarks.csv")
        print(df)
            
        b.execute("SELECT * FROM `moz_annos` ;")
        cols = [column[0] for column in b.description]
        datadf = pd.DataFrame.from_records(data=b.fetchall(), columns=cols )
        conn.close()
        df = pd.DataFrame(datadf)
        df.to_csv(firefoxpath + "downloads.csv", sep='\t', escapechar='\b', header=False, index=False)
        print(df)
            
    elif arge.all:
        allpath = os.path.join("C:/Users/",username,"Desktop/forensic_artifact/All_history/")
        os.makedirs(allpath, exist_ok=True)
            
        f.execute("SELECT * FROM urls")
        cols = [column[0] for column in f.description] # 컬럼 가져옴
        datadf = pd.DataFrame.from_records(data=f.fetchall(), columns=cols)
        df = pd.DataFrame(datadf)
        df.to_csv(allpath + "urls_chrome.csv")
            
        f.execute("SELECT * FROM `keyword_search_terms` ;")
        cols = [column[0] for column in f.description]
        datadf = pd.DataFrame.from_records(data=f.fetchall(), columns=cols)
        df = pd.DataFrame(datadf)
        df.to_csv(allpath + "keyword_search_terms_chrome.csv")
        print(df)
            
        f.execute("SELECT * FROM `downloads` ;")
        cols = [column[0] for column in f.description]
        datadf = pd.DataFrame.from_records(data=f.fetchall(), columns=cols )
            
        df = pd.DataFrame(datadf)
        df.to_csv(allpath + "downloads_chrome.csv", sep='\t', escapechar='\b', header=False, index=False)
        print(df)
    

            
        s.execute("SELECT * FROM `urls` ;")
        cols = [column[0] for column in s.description] # 컬럼 가져옴
        datadf = pd.DataFrame.from_records(data=s.fetchall(), columns=cols)
        df = pd.DataFrame(datadf)
        df.to_csv(allpath + "urls_edge.csv")
            
        s.execute("SELECT * FROM `keyword_search_terms` ;")
        cols = [column[0] for column in s.description]
        datadf = pd.DataFrame.from_records(data=s.fetchall(), columns=cols)
        df = pd.DataFrame(datadf)
        df.to_csv(allpath + "keyword_search_terms_edge.csv")
        print(df)
            
        s.execute("SELECT * FROM `downloads` ;")
        cols = [column[0] for column in s.description]
        datadf = pd.DataFrame.from_records(data=s.fetchall(), columns=cols )
           
        df = pd.DataFrame(datadf)
        df.to_csv(allpath + "downloads_edge.csv", sep='\t', escapechar='\b', header=False, index=False)
        print(df)
        
     
        b.execute("SELECT * FROM `moz_places` ;")
        cols = [column[0] for column in b.description] # 컬럼 가져옴
        datadf = pd.DataFrame.from_records(data=b.fetchall(), columns=cols)
        df = pd.DataFrame(datadf)
        df.to_csv(firefoxpath + "urls.csv")
            
            
        b.execute("SELECT * FROM `moz_bookmarks` ;")
        cols = [column[0] for column in b.description]
        datadf = pd.DataFrame.from_records(data=b.fetchall(), columns=cols)
        df = pd.DataFrame(datadf)
        df.to_csv(firefoxpath + "bookmarks.csv")
        print(df)
            
        b.execute("SELECT * FROM `moz_annos` ;")
        cols = [column[0] for column in b.description]
        datadf = pd.DataFrame.from_records(data=b.fetchall(), columns=cols )
        conn.close()
        df = pd.DataFrame(datadf)
        df.to_csv(firefoxpath + "downloads.csv", sep='\t', escapechar='\b', header=False, index=False)
        print(df)
            
if __name__ == '__main__':
            parser_argument()