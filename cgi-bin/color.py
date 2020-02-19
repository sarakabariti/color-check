import cgi
form = cgi.FieldStorage()
color = form.getvalue('color')

def check_color():
    colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange']
    if color in colors:
        return(f"{color} is a color!")
    else: 
        return(f"{color} is not a color!")

print(f'''
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Check Color!</title>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    
    <!-- import the webpage's stylesheet -->
    <link rel="stylesheet" href="/style.css">
    
    <!-- import the webpage's javascript file -->
    <script src="/script.js" defer></script>
  </head>  
  <body>
    <h1>Checking color...!</h1>
    
    <p>
      {check_color()}
      <form action="" method="get" class="form-example">
      <div class="form-example">
      <label for="color">Enter a color: </label>
      <input type="text" name="color" id="color" required>
      </div>
      </form>
    </p>

  </body>
</html>
''')
