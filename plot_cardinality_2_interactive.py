import pandas as pd
import plotly.graph_objects as go


def build_and_save_interactive_plot(csv_path="reversed_dickson_values.csv", out_html="cardinality_2_indices_interactive.html"):
    # Load data
    df = pd.read_csv(csv_path)
    df2 = df[df["value_count"] == 2].copy()
    if df2.empty:
        print("No rows with value_count == 2 found in", csv_path)
        return

    # Prepare lists for each pattern
    pattern1_data = []  # n = (p^2+1)/2
    pattern2_data = []  # n = p^2-1
    pattern3_data = []  # n = (p^2+2p-1)/2

    for p, group in df2.groupby("p"):
        n_values = sorted(group["n"].tolist())

        n1 = (p ** 2 + 1) // 2
        base_n2 = (p ** 2 - 1) // 2

        # Pattern 1
        if n1 in n_values:
            pattern1_data.append((p, n1))
            n_values.remove(n1)

        # Pattern 2 (multiple of base_n2)
        found_n2 = None
        for n in list(n_values):
            if base_n2 > 0 and n % base_n2 == 0:
                found_n2 = n
                break
        if found_n2 is not None:
            pattern2_data.append((p, found_n2))
            n_values.remove(found_n2)

        # The remaining n is the "third n"; prefer the unified closed-form if present
        n3 = (p ** 2 + 2 * p - 1) // 2
        if n3 in n_values:
            third_n = n3
            n_values.remove(n3)
            pattern3_data.append((p, third_n))
        elif n_values:
            # Fallback to any leftover value
            third_n = n_values[0]
            pattern3_data.append((p, third_n))

    # Create traces for the plot
    traces = []

    # Pattern 1
    if pattern1_data:
        ps, ns = zip(*pattern1_data)
        traces.append(go.Scatter(
            x=ps, y=ns, mode='markers', name='n = (p^2+1)/2',
            hovertemplate='p=%{x}<br>n=%{y}'
        ))

    # Pattern 2
    if pattern2_data:
        ps, ns = zip(*pattern2_data)
        traces.append(go.Scatter(
            x=ps, y=ns, mode='markers', name='n = p²-1',
            hovertemplate='p=%{x}<br>n=%{y}'
        ))

    # Pattern 3 (Unified)
    if pattern3_data:
        ps, ns = zip(*pattern3_data)
        traces.append(go.Scatter(
            x=ps, y=ns, mode='markers', name='n = (p²+2p-1)/2',
            hovertemplate='p=%{x}<br>n=%{y}'
        ))

    # Create the figure
    fig = go.Figure(data=traces)

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
