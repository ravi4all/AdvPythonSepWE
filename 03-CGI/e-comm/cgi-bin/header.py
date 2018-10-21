#!C:/Python36/python.exe

def head(reg, name):
    if reg:
        value = "<h3>Welcome {}</h3>".format(name)
    else:
        value = """
              <!-- Button trigger modal -->
        <button type="button" class="btn btn-success" data-toggle="modal" data-target="#exampleModal">
          Login
        </button>

        <!-- Modal -->
        <div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
          <div class="modal-dialog" role="document">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel">Login Form</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                  <span aria-hidden="true">&times;</span>
                </button>
              </div>
              <div class="modal-body">
                <form action='login.py' method='post'>
          <div class="form-group">
            <label for="exampleInputEmail1">Email address</label>
            <input type="email" name='email' class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email">
            <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>
          </div>
          <div class="form-group">
            <label for="exampleInputPassword1">Password</label>
            <input type="password" name='pwd' class="form-control" id="exampleInputPassword1" placeholder="Password">
          </div>
          <div class="form-group form-check">
            <input type="checkbox" class="form-check-input" id="exampleCheck1">
            <label class="form-check-label" for="exampleCheck1">Check me out</label>
          </div>
          <button type="submit" class="btn btn-primary">Submit</button>
        </form>
              </div>
            </div>
          </div>
        </div>

              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
              <!-- Button trigger modal -->
        <button type="button" class="btn btn-success" data-toggle="modal" data-target="#exampleModal_1">
          Register
        </button>

              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

        <!-- Modal -->
        <div class="modal fade" id="exampleModal_1" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
          <div class="modal-dialog" role="document">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel1">Registration Form</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                  <span aria-hidden="true">&times;</span>
                </button>
              </div>
              <div class="modal-body">
                <form action="register.py" method="post">
                    <div class="form-group">
            <label for="exampleInputName1">Enter Name</label>
            <input type="text" name="u_name" class="form-control" id="exampleInputName1" placeholder="Enter Name">
          </div>
          <div class="form-group">
            <label for="exampleInputEmail1">Email address</label>
            <input type="email" name="u_email" class="form-control" id="exampleInputEmail2" aria-describedby="emailHelp" placeholder="Enter email">
            <small id="emailHelp1" class="form-text text-muted">We'll never share your email with anyone else.</small>
          </div>
          <div class="form-group">
            <label for="exampleInputPassword1">Password</label>
            <input type="password" name="u_pwd" class="form-control" id="exampleInputPassword2" placeholder="Password">
          </div>
                    <div class="form-group">
            <label for="exampleInputPhone1">Enter Mobile No</label>
            <input type="text" name="u_num" class="form-control" id="exampleInputPhone1" placeholder="Enter Mobile No">
          </div>
                    <div class="form-group">
            <label for="exampleInputCity1">Enter City</label>
            <select class="form-control" name="u_city" id="exampleInputCity1">
                <option>Choose City</option>
                <option value="del">Delhi</option>
                <option value="mum">Mumbai</option>
                <option value="gzb">Ghaziabad</option>
                <option value="pune">Pune</option>
            </select>
          </div>

          <button type="submit" class="btn btn-primary">Submit</button>
        </form>
              </div>
            </div>
          </div>
        </div>
        """


    print("""
    <!doctype html>
    <html lang="en">
      <head>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
        <link rel='stylesheet' href='../stylesheet/main.css'>
        <title>Hello, world!</title>
      </head>
      <body>

      <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
      <a class="navbar-brand" href="#">Navbar</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item active">
            <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Sports</a>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
              Electronics
            </a>
            <div class="dropdown-menu" aria-labelledby="navbarDropdown">
              <a class="dropdown-item" href="#">Mobile</a>
              <a class="dropdown-item" href="#">Tabs</a>
              <a class="dropdown-item" href="#">TV</a>
            </div>
          </li>
            <li class="nav-item">
            <a class="nav-link" href="#">Books</a>
          </li>
        </ul>
    """)

    print("""{} &nbsp;&nbsp;""".format(value))

    print("""
          <form class="form-inline my-2 my-lg-0" action='search.py'>
          <input name='product' class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
          <button class="btn btn-danger my-2 my-sm-0" type="submit">Search</button>
        </form>
      </div>
    </nav>
    """)