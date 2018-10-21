import cgi
import json
import header

form = cgi.FieldStorage()
product = form.getvalue('product')

header.head(False, "")

print("""
<div class='container'>
<h1>Search Result for {}</h1>
<hr>
<ul style='display:flex; flex-wrap:wrap;'>
""".format(product))

with open('data.json') as file:
    data = json.load(file)

    for row in data:
        if product.lower() in row['p_name'].lower():
            print("""<li class='list-group-item'> <img src={} class='pImage' style='width:50%;'>
                                        <p>{} Price : {}</p>
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