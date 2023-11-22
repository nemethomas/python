# python
Ich möchte auf meinem Raspberry mit Python entwickeln. Dazu möchte ich webdiagramme entwickeln welche ich von meinem Rechner aus aufrufen kann. 

1) Ich setze einen Raspberry auf und hänge ihn ins LAN.
2) Ich installiere plotly biblothek: pip install plotly
3) Um Python-Code auszuführen, müssen Sie diesen in einem Python-Interpreter starten mit: python3
4) import plotly.graph_objects as go
5) Erstellen eines einfachen Plotly-Diagramms: fig = go.Figure(data=go.Bar(y=[2, 3, 1]))
6) Speichern des Diagramms als HTML-Datei: fig.write_html('/home/janos/Desktop/test.html')
7) Um von meinem Rechner über den browser das html anschauen zu können: python3 -m http.server 8080
8) Danach von meinem Rechner http://192.168.178.47:8000/test.html
