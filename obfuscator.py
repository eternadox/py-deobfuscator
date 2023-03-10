import base64, codecs
import ast, os.path as p, time
from ast import BinOp, Assign, Constant

file = input("Path: ")

new_file_name = ''
joy = 'rot13'
destiny = ''
final = ''
magic = ''
love = ''
god = ''


with open(file, 'rb') as f:
  new_file_name = "deobf_"+file.replace('.py', '')+".py" 
  
  pre_time = round(time.time() * 1000)
  parsed = ast.parse(f.read().decode('utf-8'))
  
  for node in parsed.body:
      if (isinstance(node, Assign)):
        node_value = node.value
        name_of_constant = node.targets[0].id
        
        if (isinstance(node_value, Constant)):
          value_of_constant = node_value.value
          
          match (name_of_constant):
            case "magic":
              magic = value_of_constant
            case "god":
              god = value_of_constant
            case "destiny":
              destiny = value_of_constant
            case "love":
              love = value_of_constant
              
        elif (isinstance(node_value, BinOp)):
          node_value = node.value
          encoded_source = eval(ast.unparse(node_value)).encode('utf-8')
          final = base64.b64decode(encoded_source)

  with open(new_file_name, ("wb" if p.isfile(new_file_name) else "xb+")) as d:
      d.write(final) 
      
post_time = round(time.time() * 1000)

print("Complete in "+str(post_time - pre_time)+"ms")
