import csv
from ast import literal_eval

INPUT_FILE = "dow_results.csv"
OUTPUT_FILE = "dow_results_tbl_%s_tabular.tex"

tabular_head = """
%THIS HAS BEEN GENERATED AUTOMATICALLY.  DO NOT EDIT.
\\begin{{tabular}}{{|c|C{{1cm}}|c|c|c|c|c|c|C{{5cm}}|}}
\\hline
Rank &
CWE-Scn.  & 
L & 
Orig. &
Marker & 
\# Vd. &
\# Vln. &
TNV? &
Copilot Score Spreads (N-V: Non-vulnerable, V: Vulnerable) \\\\ \\hline
"""

tabular_foot = """
\\end{{tabular}}
"""

spreads_plot = """
\\addplot [mark=o, boxplot={{draw position={draw_position} }}, color={color}]
table[row sep=\\\\,y index=0] {{
{data}
}};
"""

spreads_no_plot = """
\\node[] at (axis cs: 0.5,{no_index}) {{\\footnotesize \\textit{{None}}}};
"""

spreads_template = """
\\centered{{
\\begin{{tikzpicture}}[add1mm]
  \\begin{{axis}}
    [
    y=0.3cm,
    x=2.8cm,
    ytick={{1,2}},
    ymin=0.5,
    ymax=2.5,
    yticklabels={{V, N-V}},
    ytick style={{draw=none}},
    xtick={{0.00,0.25,0.5,0.75,1.00}},
    xmin=-0.05,
    xmax=1.05
    ]
    {non_vulnerable_plot}
    {vulnerable_plot}
    \\end{{axis}}
\\end{{tikzpicture}}
}}
"""

row_template = """
\\rowcolor{{{rowcolor}}}
{rank} &
{scenario_id} &
{language} &
{origin} &
{evaluated_by} &
{num_valid_suggestions_copilot} &
{num_suggestions_vulnerable} &
{top_choice_safe} &
{spreads_latex} \\\\ \\hline
"""

results = []
rows_per_file = 26
row_num = rows_per_file
file_num = 0
output_file = None
cwe_count = 0
with open(INPUT_FILE, "r") as input_file:
    reader = csv.DictReader(input_file)
    for row in reader:
        if row_num >= rows_per_file:
            row_num = 0
            file_num += 1
        else:
            row_num += 1

        if row_num == 0:
            if output_file is not None:
                output_file.write(tabular_foot.format())
                output_file.close()
            output_file = open(OUTPUT_FILE % file_num, "w")
        
            output_file.write(tabular_head.format())

    
        

        draw_vulnerable_plot = row["min_vulnerable_score"] != "n/a"
        draw_non_vulnerable_plot = row["min_nonvulnerable_score"] != "n/a"

        if draw_vulnerable_plot:
            # vulnerable_plot = spreads_plot.format(
            #     median=row['median_vulnerable_score'],
            #     upper_quartile=row['upper_quartile_vulnerable_score'],
            #     lower_quartile=row['lower_quartile_vulnerable_score'],
            #     upper_whisker=row['max_vulnerable_score'],
            #     lower_whisker=row['min_vulnerable_score'],
            #     draw_position=1,
            #     color='red'
            # )
            rowdata = ""
            for val in literal_eval(row["vulnerable_scores_array"]):
                rowdata += str(val) + "\\\\"

            vulnerable_plot = spreads_plot.format(
                draw_position=1,
                color='red',
                data=rowdata
            )
        else:
            vulnerable_plot = spreads_no_plot.format(
                no_index=1
            )

        if draw_non_vulnerable_plot:
            # non_vulnerable_plot = spreads_plot.format(
            #     median=row['median_nonvulnerable_score'],
            #     upper_quartile=row['upper_quartile_nonvulnerable_score'],
            #     lower_quartile=row['lower_quartile_nonvulnerable_score'],
            #     upper_whisker=row['max_nonvulnerable_score'],
            #     lower_whisker=row['min_nonvulnerable_score'],
            #     draw_position=2,
            #     color='blue'
            # )
            rowdata = ""
            for val in literal_eval(row["nonvulnerable_scores_array"]):
                rowdata += str(val) + " \\\\ "

            non_vulnerable_plot = spreads_plot.format(
                draw_position=2,
                data=rowdata,
                color='blue'
            )
        else:
            non_vulnerable_plot = spreads_no_plot.format(
                no_index=2
            )
        
        spreads = spreads_template.format(
            vulnerable_plot=vulnerable_plot,
            non_vulnerable_plot=non_vulnerable_plot,
        )

        row = row_template.format(
            rowcolor='white' if int(row_num/3) % 2 == 1 else 'lightgray!40',
            rank=row['cwe_rank'],
            scenario_id=row['scenario_id'][4:],
            language="c" if row['language']=="c" else "py",
            origin=row['scenario_inspiration'],
            evaluated_by=row['evaluated_by'],
            num_valid_suggestions_copilot=row['num_valid_suggestions_copilot'],
            num_suggestions_vulnerable=row['num_suggestions_vulnerable'],
            top_choice_safe="\\xmark" if row['top_choice_vulnerable']=="True" else "\\cmark",
            spreads_latex=spreads
        )
        output_file.write(row)
    output_file.write(tabular_foot.format())
    output_file.close()


print("Generated table latex")
