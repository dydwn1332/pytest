from flask import Flask, render_template, Response, request
import video_feed
import video_feed_copy
import os
import threading
app = Flask(__name__)


@app.route('/')
def index():
    # HTML 페이지 반환
    return render_template('index.html')


@app.route('/video_events', methods=['POST'])
def video_events_route():
    if request.method == 'POST':
        title = request.form.get('id')
        print(title)

    videoNames = os.listdir("static/videos")
    videoNames.sort()
    return render_template('video_events.html', names=videoNames,
                           title="url_for('static', filename='video/2023-05-16-13:30:55.mp4')")


@app.route('/video_feed')
def video_feed_route():
    # HTTP 응답으로 스트리밍 비디오 반환
    return Response(video_feed.video_feed(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


t1 = threading.Thread(target=video_feed_copy.video_feed)
t1.start()
app.run(host='192.168.1.102', debug=True)
