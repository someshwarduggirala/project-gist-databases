from .models import Gist

def search_gists(db_connection, **kwargs):
    
    predicate={
        "github_id":"github_id=:github_id"
        ,"created_at":"datetime(created_at)=datetime(:created_at)"
        ,"created_at__gt":"datetime(created_at)>datetime(:created_at__gt)"
        ,"created_at__gte":"datetime(created_at)>=datetime(:created_at__gte)"
        ,"created_at__lt":"datetime(created_at)<datetime(:created_at__lt)"
        ,"created_at__lte":"datetime(created_at)<=datetime(:created_at__lte)"
        ,"updated_at__gt":"datetime(updated_at)>datetime(:updated_at__gt)"
        ,"updated_at__gte":"datetime(updated_at)>=datetime(:updated_at__gte)"
        ,"updated_at__lt":"datetime(updated_at)<datetime(:updated_at__lt)"
        ,"updated_at__lte":"datetime(updated_at)<=datetime(:updated_at__lte)"
 
    }
    
    
    predicate_list=[]
    for compareop in kwargs:
        if compareop in predicate:
            predicate_list.append(predicate[compareop])
    
    if predicate_list:
        where_clause="WHERE " + " AND ".join(predicate_list)
    else:
        where_clause=""
    
    
    gists_data=db_connection.execute("select * from gists " + where_clause,kwargs)
    gists_list=[]
    for gist_data in gists_data:
        gists_list.append(Gist(gist_data))
        
    
    return gists_list
