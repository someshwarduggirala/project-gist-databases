import requests
#import sqlite3
def import_gists_to_database(db, username, commit=True):
    
    
    ## retrieve gists of a user
    gist_data=requests.get("https://api.github.com/users/{user}/gists".format(user=username))
    gist_data.raise_for_status()

    gist_insert_list=[]
    for gists in gist_data.json():
        
        gist_insert_list.append((gists["id"],
                                gists["html_url"],
                                gists["git_pull_url"],
                                gists["git_push_url"],                        
                                gists["commits_url"],
                                gists["forks_url"],
                                gists["public"],
                                gists["created_at"],
                                gists["updated_at"],
                                gists["comments"],
                                gists["comments_url"]
                                )
                               )


    ##Create the database schema  
    with open("../schema.sql","r") as schema:
        ddl_script=schema.read()
    
    db.executescript(ddl_script)
    db.executemany("""INSERT INTO gists (github_id
  ,html_url
  ,git_pull_url
  ,git_push_url
  ,commits_url
  ,forks_url 
  ,public
  ,created_at
  ,updated_at
  ,comments
  ,comments_url) VALUES (?,?,?,?,?,?,?,?,?,?,?)""",gist_insert_list)
    
    if commit:
        db.commit()
    
    
#db=sqlite3.connect('sample.db')
#import_gists_to_database(db,'gvanrossum')
#print(db.execute("select * from gists").fetchall())



"""
  github_id
  ,html_url
  ,git_pull_url
  ,git_push_url
  ,commits_url
  ,forks_url 
  ,public
  ,created_at
  ,updated_at
  ,comments
  ,comments_url
  """