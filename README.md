# restapi

REST-API
========
Models:
  Purchaser
    - id
    - name
    - created timestamp

  Product
   - id
   - name
   - timestamp


Endpoints:
  POST /purchaser
    - sample body {"name":"bob"}

  POST /product
    - sample body {"name":"xyz"}

  POST /purchaser-product
    - sample body {
                     "purchaser-id":1
                     "product-id":2
                     "purchased-timestamp":2019/08/27 10:58:31
                  }

  GET /purchaser/${purchaser-id}/product?start_date={$start_date}&end_date={$end_date}
    - sample body {
                    "purchases" : {
                      "2019-05-10": [
                        { 
                          "product" : "cake"
                        },
                        {
                          "product" : "trumpet"
                        }
                      ],
                      "2019-05-09": [
                        {
                          "product" : "trumpet"
                        }
                      ],
                      "2019-05-08": [
                        {
                          "product" : "candles"
                        }
                      ]
                    }
                  }
