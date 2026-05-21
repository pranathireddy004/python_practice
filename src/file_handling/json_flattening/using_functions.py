#using functions
orders={
  "order_id": 101,
  "customer": {
    "name": "Pranathi",
    "city": "Hyderabad"
  },
  "payment": {
    "method": "UPI",
    "amount": 2500
  }
}
flat={}
def flatten_json(data,pk=''):
    for key,values in data.items():
        if pk:
            new_key=pk+'_'+key
        else:
            new_key=key
        if isinstance(values,dict):
            flatten_json(values,new_key)
        else:
            flat[new_key]=values
    return flat
print(flatten_json(orders,''))



