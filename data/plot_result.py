import os

import plotly.graph_objects as go
import ujson as json


def get_figure(data, x_label):
    params = [item[x_label] for item in data]

    response_time_fig = go.Figure(
        data=[
            go.Bar(
                name="drl", x=params, y=[item["response_time"]["drl"] for item in data]
            ),
            go.Bar(
                name="random",
                x=params,
                y=[item["response_time"]["random"] for item in data],
            ),
            go.Bar(
                name="round_robin",
                x=params,
                y=[item["response_time"]["round_robin"] for item in data],
            ),
            go.Bar(
                name="earliest",
                x=params,
                y=[item["response_time"]["earliest"] for item in data],
            ),
        ]
    )
    response_time_fig.update_layout(
        barmode="group", xaxis_title=x_label, yaxis_title="average_response_time"
    )

    cost_fig = go.Figure(
        data=[
            go.Bar(name="drl", x=params, y=[item["cost"]["drl"] for item in data]),
            go.Bar(
                name="random", x=params, y=[item["cost"]["random"] for item in data]
            ),
            go.Bar(
                name="round_robin",
                x=params,
                y=[item["cost"]["round_robin"] for item in data],
            ),
            go.Bar(
                name="earliest", x=params, y=[item["cost"]["earliest"] for item in data]
            ),
        ]
    )
    cost_fig.update_layout(barmode="group", xaxis_title=x_label, yaxis_title="cost")

    return response_time_fig, cost_fig


with open("result.json") as f:
    data = json.load(f)

# vary lambda
collected = []
for result in data["results"]:
    if result["job_io_proportion"] == 0.5 and result["vm_io_proportion"] == 0.5:
        collected.append(result)

fig1, fig2 = get_figure(collected, "lambda")
fig1.show()
fig2.show()

# vary job_io_proportion
collected = []
for result in data["results"]:
    if result["lambda"] == 20.0 and result["vm_io_proportion"] == 0.5:
        collected.append(result)

fig1, fig2 = get_figure(collected, "job_io_proportion")
fig1.show()
fig2.show()

# vary vm_io_proportion
collected = []
for result in data["results"]:
    if result["lambda"] == 20.0 and result["job_io_proportion"] == 0.5:
        collected.append(result)

fig1, fig2 = get_figure(collected, "vm_io_proportion")
fig1.show()
fig2.show()
