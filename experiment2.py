import pandas as pd
from math import sqrt
import matplotlib.pyplot as plt
import cumming_plot


######################################
# IMPORT DATA, TIDY, DESCRIPTIVE STATS
######################################

# Import data
exp2 = pd.read_csv('exp2_data.txt', index_col=0)

# Convert gender and handedness to category
exp2.loc[:, 'gender'] = exp2.loc[:, 'gender'].astype('category')
exp2.loc[:, 'handedness'] = exp2.loc[:, 'handedness'].astype('category')

# Calculate difference scores condition - control

# Temperature - spacing
exp2['cold_start_diff_sp'] = exp2.cold_start_sp - exp2.temp_start_sp
exp2['hot_start_diff_sp'] = exp2.hot_start_sp - exp2.temp_start_sp
exp2['cold_end_diff_sp'] = exp2.cold_end_sp - exp2.temp_end_sp
exp2['hot_end_diff_sp'] = exp2.hot_end_sp - exp2.temp_end_sp

exp2['cold_time_diff_sp'] = exp2.cold_end_diff_sp - exp2.cold_start_diff_sp
exp2['hot_time_diff_sp'] = exp2.hot_end_diff_sp - exp2.hot_start_diff_sp

# Temperature - ownership
exp2['cold_start_diff_own'] = exp2.cold_start_own - exp2.temp_start_own
exp2['hot_start_diff_own'] = exp2.hot_start_own - exp2.temp_start_own
exp2['cold_end_diff_own'] = exp2.cold_end_own - exp2.temp_end_own
exp2['hot_end_diff_own'] = exp2.hot_end_own - exp2.temp_end_own

exp2['cold_time_diff_own'] = exp2.cold_end_diff_own - exp2.cold_start_diff_own
exp2['hot_time_diff_own'] = exp2.hot_end_diff_own - exp2.hot_start_diff_own

# texture - spacing
exp2['smooth_start_diff_sp'] = exp2.smooth_start_sp - exp2.text_start_sp
exp2['rough_start_diff_sp'] = exp2.rough_start_sp - exp2.text_start_sp
exp2['smooth_end_diff_sp'] = exp2.smooth_end_sp - exp2.text_end_sp
exp2['rough_end_diff_sp'] = exp2.rough_end_sp - exp2.text_end_sp

exp2['rough_time_diff_sp'] = exp2.rough_end_diff_sp - exp2.rough_start_diff_sp
exp2['smooth_time_diff_sp'] = exp2.smooth_end_diff_sp - exp2.smooth_start_diff_sp

# texture - ownership
exp2['smooth_start_diff_own'] = exp2.smooth_start_own - exp2.text_start_own
exp2['rough_start_diff_own'] = exp2.rough_start_own - exp2.text_start_own
exp2['smooth_end_diff_own'] = exp2.smooth_end_own - exp2.text_end_own
exp2['rough_end_diff_own'] = exp2.rough_end_own - exp2.text_end_own

exp2['rough_time_diff_own'] = exp2.rough_end_diff_own - exp2.rough_start_diff_own
exp2['smooth_time_diff_own'] = exp2.smooth_end_diff_own - exp2.smooth_start_diff_own

# Shape - spacing
exp2['square_start_diff_sp'] = exp2.square_start_sp - exp2.shape_start_sp
exp2['odd_start_diff_sp'] = exp2.odd_start_sp - exp2.shape_start_sp
exp2['square_end_diff_sp'] = exp2.square_end_sp - exp2.shape_end_sp
exp2['odd_end_diff_sp'] = exp2.odd_end_sp - exp2.shape_end_sp

exp2['odd_time_diff_sp'] = exp2.odd_end_diff_sp - exp2.odd_start_diff_sp
exp2['square_time_diff_sp'] = exp2.square_end_diff_sp - exp2.square_start_diff_sp

# Shape - ownership
exp2['square_start_diff_own'] = exp2.square_start_own - exp2.shape_start_own
exp2['odd_start_diff_own'] = exp2.odd_start_own - exp2.shape_start_own
exp2['square_end_diff_own'] = exp2.square_end_own - exp2.shape_end_own
exp2['odd_end_diff_own'] = exp2.odd_end_own - exp2.shape_end_own

exp2['odd_time_diff_own'] = exp2.odd_end_diff_own - exp2.odd_start_diff_own
exp2['square_time_diff_own'] = exp2.square_end_diff_own - exp2.square_start_diff_own

# Firmness - spacing
exp2['firm_start_diff_sp'] = exp2.firm_start_sp - exp2.firmness_start_sp
exp2['soft_start_diff_sp'] = exp2.soft_start_sp - exp2.firmness_start_sp
exp2['firm_end_diff_sp'] = exp2.firm_end_sp - exp2.firmness_end_sp
exp2['soft_end_diff_sp'] = exp2.soft_end_sp - exp2.firmness_end_sp

exp2['firm_time_diff_sp'] = exp2.firm_end_diff_sp - exp2.firm_start_diff_sp
exp2['soft_time_diff_sp'] = exp2.soft_end_diff_sp - exp2.soft_start_diff_sp

# Firmness - ownership
exp2['firm_start_diff_own'] = exp2.firm_start_own - exp2.firmness_start_own
exp2['soft_start_diff_own'] = exp2.soft_start_own - exp2.firmness_start_own
exp2['firm_end_diff_own'] = exp2.firm_end_own - exp2.firmness_end_own
exp2['soft_end_diff_own'] = exp2.soft_end_own - exp2.firmness_end_own

exp2['firm_time_diff_own'] = exp2.firm_end_diff_own - exp2.firm_start_diff_own
exp2['soft_time_diff_own'] = exp2.soft_end_diff_own - exp2.soft_start_diff_own

# Loop through items in dataframe and calculate basic summary statistics
txt = ['{:<15} {}'.format('Male', sum(exp2.gender == 'male')),
       '{:<15} {}'.format('Female', sum(exp2.gender == 'female')),
       '{:<15} {}'.format('Right handed', sum(exp2.handedness == 'right')),
       '{:<15} {}'.format('Left handed', sum(exp2.handedness == 'left')),
       '{:<15} mean = {:>4.1f}   SD = {:>3.1f}   min = {:>2.0f}   '
       'max = {:>2.0f}'.format('age', exp2['age'].mean(),
                               exp2['age'].std(), exp2['age'].min(), exp2['age'].max())]


for line in txt:
    print(line)

for loop, line in enumerate(txt):
    if loop == 0:
        flag = 'w'
    else:
        flag = 'a'
    with open('exp2_results.txt', flag) as file:
        file.write(line)
        file.write('\n')

with open('exp2_results.txt', flag) as file:
    file.write('\n')
    file.write('='*7)
    file.write('\nSPACING\n')
    file.write('='*7)
    file.write('\n'*2)

for i in exp2:
    if exp2[i].dtypes == 'float64':
        txt = '{:>22}  count = {:<2.0f}   mean = {:>4.1f}   SD = {:>3.1f}   95% MoE = {:>4.2f}   95%CI = {:>5.2f} to {:>5.2f}  min = {:>2.0f}   ' \
              'max = {:>2.0f}'.format(i, exp2[i].count(), exp2[i].mean(), exp2[i].std(), (exp2[i].std() / sqrt(len(exp2[i]))) * 1.96,
                                      exp2[i].mean() - (exp2[i].std() / sqrt(len(exp2[i]))) * 1.96,
                                      exp2[i].mean() + (exp2[i].std() / sqrt(len(exp2[i]))) * 1.96,
                                      exp2[i].min(), exp2[i].max())
        print(txt)
        with open('exp2_results.txt', 'a') as file:
            file.write(txt)
            file.write('\n')

with open('exp2_results.txt', flag) as file:
    file.write('\n')
    file.write('='*9)
    file.write('\nOWNERSHIP\n')
    file.write('='*9)
    file.write('\n'*2)
for i in exp2:
    if exp2[i].dtypes == 'int64':
        if not i == 'age':
            txt = '{:>22}  count = {:<2.0f}   mean = {:>4.1f}   SD = {:>3.1f}   95% MoE = {:>3.2f}   95%CI = {:>5.2f} to {:>5.2f}' \
                  '   min = {:>2.0f}   max = {:>2.0f}'.format(i, exp2[i].count(), exp2[i].mean(), exp2[i].std(),
                                                              (exp2[i].std() / sqrt(len(exp2[i]))) * 1.96,
                                                              exp2[i].mean() - (exp2[i].std() / sqrt(len(exp2[i]))) * 1.96,
                                                              exp2[i].mean() + (exp2[i].std() / sqrt(len(exp2[i]))) * 1.96,
                                                              exp2[i].min(), exp2[i].max())
            print(txt)
            with open('exp2_results.txt', 'a') as file:
                file.write(txt)
                file.write('\n')

with open('exp2_results.txt', 'a') as file:
    file.write('\n\n{:8} = {}'.format('sp', 'perceived spacing'))
    file.write('\n{:8} = {}'.format('own', 'perceived ownership'))
    file.write('\n{:8} = {}'.format('95% MoE','margin of error (one side of error bar) for 95% confidence interval'))
    file.write('\n{:8} = {}'.format('diff', 'difference, calculated as end - start'))
    file.write('\n{:8} = {}'.format('temp', 'control trial for temperature'))
    file.write('\n{:8} = {}'.format('text', 'control trial for texture'))
    file.write('\n{:8} = {}'.format('shape', 'control trial for shape'))
    file.write('\n{:8} = {}'.format('firmness', 'control trial for firmness'))

######################
# FIGURE 5 Temperature
######################

fig = plt.figure(figsize=[5, 4])
style1 = {'a': ['^', 'w', 'k'], 'b': ['^', 'w', 'k'], 'diff': ['^', 'k', 'k']}
style2 = {'a': ['^', 'w', 'k'], 'b': ['^', 'w', 'k'], 'diff': ['^', 'k', 'k']}
style3 = {'a': ['^', 'w', 'k'], 'b': ['^', 'w', 'k'], 'diff': ['^', 'k', 'k']}
style4 = {'a': ['^', 'w', 'k'], 'b': ['^', 'w', 'k'], 'diff': ['^', 'k', 'k']}
marker_size = [2, 4]
markeredgewdith = 0.4
linewidth = 1
axes_tick_width = .5
font_size = 8
letterfontsize = 10
connectcolor = '0.8'
x_spacing = [0.01, 0.015, 0.05, 0.055, 0.075]
jit = 0.0001
skip_raw_marker = True
x_axis_nudge = [-0.005, -0.005, -.005]
zero_line2 = False
ax2yticks = [-1, 2, 5]

# Subplot 2,2,1  no grasp: start-end
data = [list(exp2.hot_start_diff_sp), list(exp2.hot_end_diff_sp)]
ax1 = fig.add_subplot(2, 2, 1)
cumming_plot.paired(data, ax1,
                    yticks=[-12, 12, 4],
                    style=style1,
                    ylabel='Difference \nperceived spacing (cm)',
                    xlabel=['start', 'end', 'effect'],
                    zero_line=False,
                    y2ticks=True,
                    font_size=font_size,
                    marker_size=marker_size,
                    markeredgewidth=markeredgewdith,
                    axes_tick_width=axes_tick_width,
                    linewidth=linewidth,
                    connectcolor=connectcolor,
                    x_spacing=x_spacing,
                    jit=jit,
                    skip_raw_marker=skip_raw_marker,
                    x_axis_nudge=x_axis_nudge,
                    zero_line2=zero_line2)
plt.text(-.2, 1.15, 'A',
         horizontalalignment='center',
         fontsize=letterfontsize,
         transform=ax1.transAxes)

plt.text(0.5, 1.08, 'Hot',
         horizontalalignment='center',
         fontsize=font_size,
         transform=ax1.transAxes)

# Subplot 2,2,2  grasp: start-end
data = [list(exp2.cold_start_diff_sp), list(exp2.cold_end_diff_sp)]
ax2 = fig.add_subplot(2, 2, 2)
cumming_plot.paired(data, ax2,
                    yticks=[-12, 12, 4],
                    style=style2,
                    xlabel=['start', 'end', 'effect'],
                    zero_line=False,
                    y2ticks=True,
                    font_size=font_size,
                    marker_size=marker_size,
                    markeredgewidth=markeredgewdith,
                    axes_tick_width=axes_tick_width,
                    linewidth=linewidth,
                    connectcolor=connectcolor,
                    x_spacing=x_spacing,
                    jit=jit,
                    skip_raw_marker=skip_raw_marker,
                    x_axis_nudge=x_axis_nudge,
                    zero_line2=zero_line2)
plt.text(0.5, 1.08, 'Cold',
         horizontalalignment='center',
         fontsize=font_size,
         transform=ax2.transAxes)

# Subplot 2,2,3  start: no-grasp grasp
data = [list(exp2.hot_start_diff_own), list(exp2.hot_end_diff_own)]
ax3 = fig.add_subplot(2, 2, 3)
cumming_plot.paired(data, ax3,
                    yticks=[-8, 6, 2],
                    style=style3,
                    ylabel='Difference ownership',
                    xlabel=['start', 'end', 'effect'],
                    zero_line=False,
                    y2ticks=True,
                    font_size=font_size,
                    marker_size=marker_size,
                    markeredgewidth=markeredgewdith,
                    axes_tick_width=axes_tick_width,
                    linewidth=linewidth,
                    connectcolor=connectcolor,
                    x_spacing=x_spacing,
                    jit=jit,
                    skip_raw_marker=skip_raw_marker,
                    x_axis_nudge=x_axis_nudge,
                    zero_line2=zero_line2)
plt.text(-.2, 1.15, 'B',
         horizontalalignment='center',
         fontsize=letterfontsize,
         transform=ax3.transAxes)
plt.text(0.5, 1.08, 'Hot',
         horizontalalignment='center',
         fontsize=font_size,
         transform=ax3.transAxes)

# Subplot 2,2,4  end: no-grasp grasp
data = [list(exp2.cold_start_diff_own), list(exp2.cold_end_diff_own)]
ax4 = fig.add_subplot(2, 2, 4)
cumming_plot.paired(data, ax4,
                    yticks=[-8, 6, 2],
                    style=style4,
                    xlabel=['start', 'end', 'effect'],
                    zero_line=False,
                    y2ticks=True,
                    font_size=font_size,
                    marker_size=marker_size,
                    markeredgewidth=markeredgewdith,
                    axes_tick_width=axes_tick_width,
                    linewidth=linewidth,
                    connectcolor=connectcolor,
                    x_spacing=x_spacing,
                    jit=jit,
                    skip_raw_marker=skip_raw_marker,
                    x_axis_nudge=x_axis_nudge,
                    zero_line2=zero_line2)
plt.text(0.5, 1.08, 'Cold',
         horizontalalignment='center',
         fontsize=font_size,
         transform=ax4.transAxes)

# Adjust spacing of subplots
left = 0.15
right = 0.9
bottom = 0.05
top = 0.92
wspace = 0.5  # the amount of width reserved for blank space between subplots
hspace = 0.5  # the amount of height reserved for white space between subplots
fig.subplots_adjust(left=left, bottom=bottom, right=right, top=top, wspace=wspace, hspace=hspace)

#plt.savefig('figure5.pdf', format='pdf', dpi=600)
plt.savefig('figure5.png', format='png', dpi=600)
plt.savefig('figure5.svg', format='svg')

#####################
# FIGURE 6 Compliance
#####################

fig = plt.figure(figsize=[5, 4])
style1 = {'a': ['^', 'w', 'k'], 'b': ['^', 'w', 'k'], 'diff': ['^', 'k', 'k']}
style2 = {'a': ['^', 'w', 'k'], 'b': ['^', 'w', 'k'], 'diff': ['^', 'k', 'k']}
style3 = {'a': ['^', 'w', 'k'], 'b': ['^', 'w', 'k'], 'diff': ['^', 'k', 'k']}
style4 = {'a': ['^', 'w', 'k'], 'b': ['^', 'w', 'k'], 'diff': ['^', 'k', 'k']}
marker_size = [2, 4]
markeredgewdith = 1
linewidth = 1
axes_tick_width = .5
font_size = 8
letterfontsize = 10
connectcolor = '0.8'
x_spacing = [0.01, 0.015, 0.05, 0.055, 0.075]
jit = 0.0001
skip_raw_marker = True
x_axis_nudge = [-0.005, -0.005, -.005]
zero_line2 = False
ax2yticks = [-1, 2, 5]

# Subplot 2,2,1  no grasp: start-end
data = [list(exp2.soft_start_diff_sp), list(exp2.soft_end_diff_sp)]
ax1 = fig.add_subplot(2, 2, 1)
cumming_plot.paired(data, ax1,
                    yticks=[-10, 6, 2],
                    style=style1,
                    ylabel='Difference \nperceived spacing (cm)',
                    xlabel=['start', 'end', 'effect'],
                    zero_line=False,
                    y2ticks=True,
                    font_size=font_size,
                    marker_size=marker_size,
                    markeredgewidth=markeredgewdith,
                    axes_tick_width=axes_tick_width,
                    linewidth=linewidth,
                    connectcolor=connectcolor,
                    x_spacing=x_spacing,
                    jit=jit,
                    skip_raw_marker=skip_raw_marker,
                    x_axis_nudge=x_axis_nudge,
                    zero_line2=zero_line2)
plt.text(-.2, 1.15, 'A',
         horizontalalignment='center',
         fontsize=letterfontsize,
         transform=ax1.transAxes)

plt.text(0.5, 1.08, 'Soft',
         horizontalalignment='center',
         fontsize=font_size,
         transform=ax1.transAxes)

# Subplot 2,2,2  grasp: start-end
data = [list(exp2.firm_start_diff_sp), list(exp2.firm_end_diff_sp)]
ax2 = fig.add_subplot(2, 2, 2)
cumming_plot.paired(data, ax2,
                    yticks=[-10, 6, 2],
                    style=style2,
                    xlabel=['start', 'end', 'effect'],
                    zero_line=False,
                    y2ticks=True,
                    font_size=font_size,
                    marker_size=marker_size,
                    markeredgewidth=markeredgewdith,
                    axes_tick_width=axes_tick_width,
                    linewidth=linewidth,
                    connectcolor=connectcolor,
                    x_spacing=x_spacing,
                    jit=jit,
                    skip_raw_marker=skip_raw_marker,
                    x_axis_nudge=x_axis_nudge,
                    zero_line2=zero_line2)
plt.text(0.5, 1.08, 'Firm',
         horizontalalignment='center',
         fontsize=font_size,
         transform=ax2.transAxes)

# Subplot 2,2,3  start: no-grasp grasp
data = [list(exp2.soft_start_diff_own), list(exp2.soft_end_diff_own)]
ax3 = fig.add_subplot(2, 2, 3)
cumming_plot.paired(data, ax3,
                    yticks=[-8, 6, 2],
                    style=style3,
                    ylabel='Difference ownership',
                    xlabel=['start', 'end', 'effect'],
                    zero_line=False,
                    y2ticks=True,
                    font_size=font_size,
                    marker_size=marker_size,
                    markeredgewidth=markeredgewdith,
                    axes_tick_width=axes_tick_width,
                    linewidth=linewidth,
                    connectcolor=connectcolor,
                    x_spacing=x_spacing,
                    jit=jit,
                    skip_raw_marker=skip_raw_marker,
                    x_axis_nudge=x_axis_nudge,
                    zero_line2=zero_line2)
plt.text(-.2, 1.15, 'B',
         horizontalalignment='center',
         fontsize=letterfontsize,
         transform=ax3.transAxes)
plt.text(0.5, 1.08, 'Soft',
         horizontalalignment='center',
         fontsize=font_size,
         transform=ax3.transAxes)

# Subplot 2,2,4  end: no-grasp grasp
data = [list(exp2.firm_start_diff_own), list(exp2.firm_end_diff_own)]
ax4 = fig.add_subplot(2, 2, 4)
cumming_plot.paired(data, ax4,
                    yticks=[-8, 6, 2],
                    style=style4,
                    xlabel=['start', 'end', 'effect'],
                    zero_line=False,
                    y2ticks=True,
                    font_size=font_size,
                    marker_size=marker_size,
                    markeredgewidth=markeredgewdith,
                    axes_tick_width=axes_tick_width,
                    linewidth=linewidth,
                    connectcolor=connectcolor,
                    x_spacing=x_spacing,
                    jit=jit,
                    skip_raw_marker=skip_raw_marker,
                    x_axis_nudge=x_axis_nudge,
                    zero_line2=zero_line2)
plt.text(0.5, 1.08, 'Firm',
         horizontalalignment='center',
         fontsize=font_size,
         transform=ax4.transAxes)

# Adjust spacing of subplots
left = 0.15
right = 0.9
bottom = 0.05
top = 0.92
wspace = 0.5  # the amount of width reserved for blank space between subplots
hspace = 0.5  # the amount of height reserved for white space between subplots
fig.subplots_adjust(left=left, bottom=bottom, right=right, top=top, wspace=wspace, hspace=hspace)

#plt.savefig('figure6.pdf', format='pdf', dpi=600)
plt.savefig('figure6.png', format='png', dpi=600)
plt.savefig('figure6.svg', format='svg')

##################
# FIGURE 7 Texture
##################

fig = plt.figure(figsize=[5, 4])
style1 = {'a': ['^', 'w', 'k'], 'b': ['^', 'w', 'k'], 'diff': ['^', 'k', 'k']}
style2 = {'a': ['^', 'w', 'k'], 'b': ['^', 'w', 'k'], 'diff': ['^', 'k', 'k']}
style3 = {'a': ['^', 'w', 'k'], 'b': ['^', 'w', 'k'], 'diff': ['^', 'k', 'k']}
style4 = {'a': ['^', 'w', 'k'], 'b': ['^', 'w', 'k'], 'diff': ['^', 'k', 'k']}
marker_size = [2, 4]
markeredgewdith = 0.4
linewidth = 1
axes_tick_width = .5
font_size = 8
letterfontsize = 10
connectcolor = '0.8'
x_spacing = [0.01, 0.015, 0.05, 0.055, 0.075]
jit = 0.0001
skip_raw_marker = True
x_axis_nudge = [-0.005, -0.005, -.005]
zero_line2 = False
ax2yticks = [-1, 2, 5]

# Subplot 2,2,1  no grasp: start-end
data = [list(exp2.rough_start_diff_sp), list(exp2.rough_end_diff_sp)]
ax1 = fig.add_subplot(2, 2, 1)
cumming_plot.paired(data, ax1,
                    yticks=[-12, 16, 4],
                    style=style1,
                    ylabel='Difference \nperceived spacing (cm)',
                    xlabel=['start', 'end', 'effect'],
                    zero_line=False,
                    y2ticks=True,
                    font_size=font_size,
                    marker_size=marker_size,
                    markeredgewidth=markeredgewdith,
                    axes_tick_width=axes_tick_width,
                    linewidth=linewidth,
                    connectcolor=connectcolor,
                    x_spacing=x_spacing,
                    jit=jit,
                    skip_raw_marker=skip_raw_marker,
                    x_axis_nudge=x_axis_nudge,
                    zero_line2=zero_line2)
plt.text(-.2, 1.15, 'A',
         horizontalalignment='center',
         fontsize=letterfontsize,
         transform=ax1.transAxes)

plt.text(0.5, 1.08, 'Rough',
         horizontalalignment='center',
         fontsize=font_size,
         transform=ax1.transAxes)

# Subplot 2,2,2  grasp: start-end
data = [list(exp2.smooth_start_diff_sp), list(exp2.smooth_end_diff_sp)]
ax2 = fig.add_subplot(2, 2, 2)
cumming_plot.paired(data, ax2,
                    yticks=[-12, 16, 4],
                    style=style2,
                    xlabel=['start', 'end', 'effect'],
                    zero_line=False,
                    y2ticks=True,
                    font_size=font_size,
                    marker_size=marker_size,
                    markeredgewidth=markeredgewdith,
                    axes_tick_width=axes_tick_width,
                    linewidth=linewidth,
                    connectcolor=connectcolor,
                    x_spacing=x_spacing,
                    jit=jit,
                    skip_raw_marker=skip_raw_marker,
                    x_axis_nudge=x_axis_nudge,
                    zero_line2=zero_line2)
plt.text(0.5, 1.08, 'Smooth',
         horizontalalignment='center',
         fontsize=font_size,
         transform=ax2.transAxes)

# Subplot 2,2,3  start: no-grasp grasp
data = [list(exp2.rough_start_diff_own), list(exp2.rough_end_diff_own)]
ax3 = fig.add_subplot(2, 2, 3)
cumming_plot.paired(data, ax3,
                    yticks=[-6, 6, 2],
                    style=style3,
                    ylabel='Difference ownership',
                    xlabel=['start', 'end', 'effect'],
                    zero_line=False,
                    y2ticks=True,
                    font_size=font_size,
                    marker_size=marker_size,
                    markeredgewidth=markeredgewdith,
                    axes_tick_width=axes_tick_width,
                    linewidth=linewidth,
                    connectcolor=connectcolor,
                    x_spacing=x_spacing,
                    jit=jit,
                    skip_raw_marker=skip_raw_marker,
                    x_axis_nudge=x_axis_nudge,
                    zero_line2=zero_line2)
plt.text(-.2, 1.15, 'B',
         horizontalalignment='center',
         fontsize=letterfontsize,
         transform=ax3.transAxes)
plt.text(0.5, 1.08, 'Rough',
         horizontalalignment='center',
         fontsize=font_size,
         transform=ax3.transAxes)

# Subplot 2,2,4  end: no-grasp grasp
data = [list(exp2.smooth_start_diff_own), list(exp2.smooth_end_diff_own)]
ax4 = fig.add_subplot(2, 2, 4)
cumming_plot.paired(data, ax4,
                    yticks=[-6, 6, 2],
                    style=style4,
                    xlabel=['start', 'end', 'effect'],
                    zero_line=False,
                    y2ticks=True,
                    font_size=font_size,
                    marker_size=marker_size,
                    markeredgewidth=markeredgewdith,
                    axes_tick_width=axes_tick_width,
                    linewidth=linewidth,
                    connectcolor=connectcolor,
                    x_spacing=x_spacing,
                    jit=jit,
                    skip_raw_marker=skip_raw_marker,
                    x_axis_nudge=x_axis_nudge,
                    zero_line2=zero_line2)
plt.text(0.5, 1.08, 'Smooth',
         horizontalalignment='center',
         fontsize=font_size,
         transform=ax4.transAxes)

# Adjust spacing of subplots
left = 0.15
right = 0.9
bottom = 0.05
top = 0.92
wspace = 0.5  # the amount of width reserved for blank space between subplots
hspace = 0.5  # the amount of height reserved for white space between subplots
fig.subplots_adjust(left=left, bottom=bottom, right=right, top=top, wspace=wspace, hspace=hspace)

#plt.savefig('figure7.pdf', format='pdf', dpi=600)
plt.savefig('figure7.png', format='png', dpi=600)
plt.savefig('figure7.svg', format='svg')

################
# FIGURE 8 Shape
################

fig = plt.figure(figsize=[5, 4])
style1 = {'a': ['^', 'w', 'k'], 'b': ['^', 'w', 'k'], 'diff': ['^', 'k', 'k']}
style2 = {'a': ['^', 'w', 'k'], 'b': ['^', 'w', 'k'], 'diff': ['^', 'k', 'k']}
style3 = {'a': ['^', 'w', 'k'], 'b': ['^', 'w', 'k'], 'diff': ['^', 'k', 'k']}
style4 = {'a': ['^', 'w', 'k'], 'b': ['^', 'w', 'k'], 'diff': ['^', 'k', 'k']}
marker_size = [2, 4]
markeredgewdith = 0.4
linewidth = 1
axes_tick_width = .5
font_size = 8
letterfontsize = 10
connectcolor = '0.8'
x_spacing = [0.01, 0.015, 0.05, 0.055, 0.075]
jit = 0.0001
skip_raw_marker = True
x_axis_nudge = [-0.005, -0.005, -.005]
zero_line2 = False
ax2yticks = [-1, 2, 5]

# Subplot 2,2,1  no grasp: start-end
data = [list(exp2.odd_start_diff_sp), list(exp2.odd_end_diff_sp)]
ax1 = fig.add_subplot(2, 2, 1)
cumming_plot.paired(data, ax1,
                    yticks=[-12, 12, 4],
                    style=style1,
                    ylabel='Difference \nperceived spacing (cm)',
                    xlabel=['start', 'end', 'effect'],
                    zero_line=False,
                    y2ticks=True,
                    font_size=font_size,
                    marker_size=marker_size,
                    markeredgewidth=markeredgewdith,
                    axes_tick_width=axes_tick_width,
                    linewidth=linewidth,
                    connectcolor=connectcolor,
                    x_spacing=x_spacing,
                    jit=jit,
                    skip_raw_marker=skip_raw_marker,
                    x_axis_nudge=x_axis_nudge,
                    zero_line2=zero_line2)
plt.text(-.2, 1.15, 'A',
         horizontalalignment='center',
         fontsize=letterfontsize,
         transform=ax1.transAxes)

plt.text(0.5, 1.08, 'Odd',
         horizontalalignment='center',
         fontsize=font_size,
         transform=ax1.transAxes)

# Subplot 2,2,2  grasp: start-end
data = [list(exp2.square_start_diff_sp), list(exp2.square_end_diff_sp)]
ax2 = fig.add_subplot(2, 2, 2)
cumming_plot.paired(data, ax2,
                    yticks=[-12, 12, 4],
                    style=style2,
                    xlabel=['start', 'end', 'effect'],
                    zero_line=False,
                    y2ticks=True,
                    font_size=font_size,
                    marker_size=marker_size,
                    markeredgewidth=markeredgewdith,
                    axes_tick_width=axes_tick_width,
                    linewidth=linewidth,
                    connectcolor=connectcolor,
                    x_spacing=x_spacing,
                    jit=jit,
                    skip_raw_marker=skip_raw_marker,
                    x_axis_nudge=x_axis_nudge,
                    zero_line2=zero_line2)
plt.text(0.5, 1.08, 'Rectangular',
         horizontalalignment='center',
         fontsize=font_size,
         transform=ax2.transAxes)

# Subplot 2,2,3  start: no-grasp grasp
data = [list(exp2.odd_start_diff_own), list(exp2.square_end_diff_own)]
ax3 = fig.add_subplot(2, 2, 3)
cumming_plot.paired(data, ax3,
                    yticks=[-6, 4, 2],
                    style=style3,
                    ylabel='Difference ownership',
                    xlabel=['start', 'end', 'effect'],
                    zero_line=False,
                    y2ticks=True,
                    font_size=font_size,
                    marker_size=marker_size,
                    markeredgewidth=markeredgewdith,
                    axes_tick_width=axes_tick_width,
                    linewidth=linewidth,
                    connectcolor=connectcolor,
                    x_spacing=x_spacing,
                    jit=jit,
                    skip_raw_marker=skip_raw_marker,
                    x_axis_nudge=x_axis_nudge,
                    zero_line2=zero_line2)
plt.text(-.2, 1.15, 'B',
         horizontalalignment='center',
         fontsize=letterfontsize,
         transform=ax3.transAxes)
plt.text(0.5, 1.08, 'Odd',
         horizontalalignment='center',
         fontsize=font_size,
         transform=ax3.transAxes)

# Subplot 2,2,4  end: no-grasp grasp
data = [list(exp2.square_start_diff_own), list(exp2.square_end_diff_own)]
ax4 = fig.add_subplot(2, 2, 4)
cumming_plot.paired(data, ax4,
                    yticks=[-6, 4, 2],
                    style=style4,
                    xlabel=['start', 'end', 'effect'],
                    zero_line=False,
                    y2ticks=True,
                    font_size=font_size,
                    marker_size=marker_size,
                    markeredgewidth=markeredgewdith,
                    axes_tick_width=axes_tick_width,
                    linewidth=linewidth,
                    connectcolor=connectcolor,
                    x_spacing=x_spacing,
                    jit=jit,
                    skip_raw_marker=skip_raw_marker,
                    x_axis_nudge=x_axis_nudge,
                    zero_line2=zero_line2)
plt.text(0.5, 1.08, 'Rectangular',
         horizontalalignment='center',
         fontsize=font_size,
         transform=ax4.transAxes)

# Adjust spacing of subplots
left = 0.15
right = 0.9
bottom = 0.05
top = 0.92
wspace = 0.5  # the amount of width reserved for blank space between subplots
hspace = 0.5  # the amount of height reserved for white space between subplots
fig.subplots_adjust(left=left, bottom=bottom, right=right, top=top, wspace=wspace, hspace=hspace)

#plt.savefig('figure8.pdf', format='pdf', dpi=600)
plt.savefig('figure8.png', format='png', dpi=600)
plt.savefig('figure8.svg', format='svg')
