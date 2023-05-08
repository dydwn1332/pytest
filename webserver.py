from flask import Flask, render_template, Response
import video_feed

app = Flask(__name__)

@app.route('/')
def index():
    # HTML 페이지 반환
    return render_template('index.html')

@app.route('/video_feed')
def video_feed_route():
    # HTTP 응답으로 스트리밍 비디오 반환
    return Response(video_feed.video_feed(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


