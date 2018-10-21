import json

def products():
    with open('data.json') as file:
        data = json.load(file)
        # print(data)
        print("""
        <div class='container'>
        <ul class='products' style='display:flex; flex-wrap:wrap;'>
        """)
        with open('data.json') as data_file:
            data = json.load(data_file)
            for row in data:
                print("""<li class='list-group-item'>
                 <a href='#'>
                 <img src={} class='pImage'>
                                    <p>{} Price : {}</p></a>
                            </li>"""
                      .format(row['p_image'], row['p_name'], row['p_price']))
        print("""
        </ul>
        </div>
        """)
        print("""
        <!-- Optional JavaScript -->
                <!-- jQuery first, then Popper.js, then Bootstrap JS -->
                <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
                <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
                <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>
              </body>
            </html>
        """)

# products()