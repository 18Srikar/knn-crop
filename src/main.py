import asyncio
import tornado.web
import json

from knn_algo import predict_crop, init_model


class PredictionApiCallHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "*")
        self.set_header('Access-Control-Allow-Methods', '*')

    def options(self, *args):
        self.set_status(204)
        self.finish()

    def post(self):
        req_body = json.loads(self.request.body.decode('utf-8'))
        print(req_body)
        if "values" not in req_body or not isinstance(req_body['values'], list):
            self.write({"error": "bad request"})
            self.set_status(400)
            return
        if len(req_body['values']) != 7:
            self.write({'error': 'Invalid list length'})
            self.set_status(400)
            return
        try:
            crop_prediction = predict_crop(req_body['values'])
        except ValueError as e:
            self.write({'error': str(e)})
            self.set_status(400)
            return

        return self.write({'prediction': crop_prediction})


def make_app():
    return tornado.web.Application([
        (r"/predict", PredictionApiCallHandler)
    ])


async def main():
    print('Starting server')
    app = make_app()
    port = 8888
    app.listen(port)
    init_model()
    print(f"Server started at port {port}")
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())
