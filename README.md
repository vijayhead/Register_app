Post Method:- In request method post data is send as part of request body so data is not visible on url
            we can send secure data.
            It allows sending large amount of data.
            Post is a request used for writing data server
            Ex:-inserting, update, delete

In html file:- 
              <form action="" method="post"></form>

views.py:-
              def function(request):
                    n = request.POST['t1']
                    user = TableClass(name = n ,   ,   )               # create a object of class which imported from models.py file
                    user.save()


models.py :-
            class TableClass(models.Model):
                    name = models.CharField(max_length = 20)            #models.py file used to connectivity with database

