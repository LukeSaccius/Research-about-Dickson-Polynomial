import pandas as pd
import plotly.graph_objects as go


def build_and_save_interactive_plot(csv_path="reversed_dickson_values.csv", out_html="cardinality_2_indices_interactive.html"):
    # Load data
    df = pd.read_csv(csv_path)
    df2 = df[df["value_count"] == 2].copy()
    if df2.empty:
        print("No rows with value_count == 2 found in", csv_path)
        return

    pattern1_x = []
    pattern1_y = []
    pattern1_text = []

    pattern2_x = []
    pattern2_y = []
    pattern2_text = []

    pattern3_x = []
    pattern3_y = []
    pattern3_text = []

    for p, group in df2.groupby("p"):
        n_values = sorted(group["n"].tolist())

        n1 = (p ** 2 + 1) // 2
        base_n2 = (p ** 2 - 1) // 2

        # Pattern 1
        if n1 in n_values:
            pattern1_x.append(p)
            pattern1_y.append(n1)
            pattern1_text.append(f"p={p}<br>n={n1}<br>pattern= (p^2+1)/2")
            n_values.remove(n1)

        # Pattern 2 (multiple of base_n2)
        found_n2 = None
        for n in list(n_values):
            if base_n2 > 0 and n % base_n2 == 0:
                found_n2 = n
                break
        if found_n2 is not None:
            pattern2_x.append(p)
            pattern2_y.append(found_n2)
            pattern2_text.append(f"p={p}<br>n={found_n2}<br>pattern= k*(p^2-1)/2 (k={found_n2//base_n2})")
            n_values.remove(found_n2)

        # Whatever remains -> pattern 3
        for n in n_values:
            pattern3_x.append(p)
            pattern3_y.append(n)
            pattern3_text.append(f"p={p}<br>n={n}<br>pattern=other/conditional")

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=pattern1_x,
        y=pattern1_y,
        mode='markers',
        marker=dict(size=10, color='blue', symbol='circle'),
        name='Pattern 1: (p^2+1)/2',
        text=pattern1_text,
        hoverinfo='text'
    ))

    fig.add_trace(go.Scatter(
        x=pattern2_x,
        y=pattern2_y,
        mode='markers',
        marker=dict(size=10, color='green', symbol='square'),
        name='Pattern 2: k*(p^2-1)/2',
        text=pattern2_text,
        hoverinfo='text'
    ))

    fig.add_trace(go.Scatter(
        x=pattern3_x,
        y=pattern3_y,
        mode='markers',
        marker=dict(size=10, color='red', symbol='diamond'),
        name='Pattern 3: other (conditional)',
        text=pattern3_text,
        hoverinfo='text'
    ))

    fig.update_layout(
        title='Interactive: indices n giving cardinality 2 (hover for details)',
        xaxis_title='Prime p',
        yaxis_title='Index n',
        legend=dict(x=0.01, y=0.99),
        height=700,
    )

    # Add buttons to toggle log/linear scale for y
    fig.update_layout(
        updatemenus=[
            dict(
                type="buttons",
                direction="left",
                x=0.7,
                y=1.08,
                showactive=True,
                buttons=list([
                    dict(label="Linear Y",
                         method="relayout",
                         args=[{"yaxis.type": "linear"}]),
                    dict(label="Log Y",
                         method="relayout",
                         args=[{"yaxis.type": "log"}])
                ])
            )
        ]
    )

    fig.write_html(out_html, include_plotlyjs='cdn')
    print("Saved interactive plot to", out_html)


if __name__ == '__main__':
    build_and_save_interactive_plot()
