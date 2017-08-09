import pandas as pd
from math import sqrt
import matplotlib.pyplot as plt
import cumming_plot
import numpy as np


######################################
# IMPORT DATA, TIDY, DESCRIPTIVE STATS
######################################

# Import data
exp1 = pd.read_csv('exp1_data.txt', index_col=0)

# Convert gender and handedness to category
exp1['gender'] = exp1['gender'].astype('category')
exp1['handedness'] = exp1['handedness'].astype('category')

# Calculate difference scores [start - end]
exp1['no_grasp_diff_sp'] = exp1.no_grasp_end_sp - exp1.no_grasp_start_sp
exp1['grasp_diff_sp'] = exp1.grasp_end_sp - exp1.grasp_start_sp
exp1['grasp_diff_own'] = exp1.grasp_end_own - exp1.grasp_start_own
exp1['grasp_illusion_start_sp'] = exp1.grasp_start_sp - exp1.no_grasp_start_sp
exp1['grasp_illusion_end_sp'] = exp1.grasp_end_sp - exp1.no_grasp_end_sp
exp1['grasp_illusion_diff_sp'] = exp1.grasp_illusion_end_sp - exp1.grasp_illusion_start_sp

# Loop through items in dataframe and calculate basic summary statistics
txt = ['{:<15} {}'.format('Male', sum(exp1.gender == 'male')),
       '{:<15} {}'.format('Female', sum(exp1.gender == 'female')),
       '{:<15} {}'.format('Right handed', sum(exp1.handedness == 'right')),
       '{:<15} {}'.format('Left handed', sum(exp1.handedness == 'left')),
       '{:<15} mean = {:>4.1f}   SD = {:>3.1f}   min = {:>2.0f}   '
       'max = {:>2.0f}'.format('age', exp1['age'].mean(),
                               exp1['age'].std(), exp1['age'].min(), exp1['age'].max())]

for line in txt:
    print(line)

for loop, line in enumerate(txt):
    if loop == 0:
        flag = 'w'
    else:
        flag = 'a'
    with open('exp1_results.txt', flag) as file:
        file.write(line)
        file.write('\n')

with open('exp1_results.txt', flag) as file:
    file.write('\n')
    file.write('=' * 7)
    file.write('\nRESULTS\n')
    file.write('=' * 7)
    file.write('\n' * 2)

# Loop through items in dataframe and calculate basic summary statistics
for loop, i in enumerate(exp1):
    if exp1[i].dtypes == 'int64':
        if not i == 'age':
            txt = '{:>25}  count = {:<2.0f}  mean = {:>5.2f}  SD = {:>5.2f}  95% MoE = {:>5.2f}   ' \
                  '95%CI = {:>5.2f} to {:>5.2f}   min = {:>3.0f}   ' \
                  'max = {:>3.0f}'.format(i, exp1[i].count(), exp1[i].mean(), exp1[i].std(),
                                          (exp1[i].std()/sqrt(len(exp1[i])))*1.96,
                                          exp1[i].mean() - (exp1[i].std() / sqrt(len(exp1[i]))) * 1.96,
                                          exp1[i].mean() + (exp1[i].std() / sqrt(len(exp1[i]))) * 1.96,
                                          exp1[i].min(), exp1[i].max())
            print (txt)
            with open('exp1_results.txt', 'a') as file:
                file.write(txt)
                file.write('\n')

with open('exp1_results.txt', 'a') as file:
    file.write('\n\n{:15} = {}'.format('sp', 'perceived spacing'))
    file.write('\n{:15} = {}'.format('own', 'perceived ownership'))
    file.write('\n{:15} = {}'.format('grasp_illusion', 'difference between no-grasp and grasp'))
    file.write('\n{:15} = {}'.format('95% MoE','margin of error (one side of error bar) for 95% confidence interval'))
    file.write('\n{:15} = {}'.format('diff', 'difference, calculated as end - start'))

###########
# FIGURE 3
###########

fig = plt.figure(figsize=[5, 4])
style1 = {'a': ['o', 'w', 'k'], 'b': ['o', 'w', 'k'], 'diff': ['^', 'k', 'k']}
style2 = {'a': ['o', 'w', 'k'], 'b': ['o', 'w', 'k'], 'diff': ['^', 'k', 'k']}
style3 = {'a': ['o', 'w', 'k'], 'b': ['o', 'w', 'k'], 'diff': ['^', 'k', 'k']}
style4 = {'a': ['o', 'w',  'k'], 'b': ['o', 'w', 'k'], 'diff': ['^', 'k', 'k']}
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

# Subplot 2,2,1  no grasp: start-end
data = [list(exp1.no_grasp_start_sp.values),list(exp1.no_grasp_end_sp.values)]
ax1 = fig.add_subplot(2, 2, 1)
cumming_plot.paired(data,ax1,
                    yticks=[-10, 20, 5],
                    style=style1,
                    ylabel='Perceived spacing (cm)',
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
         transform = ax1.transAxes)

plt.text(0.5, 1.08, 'No grasp',
         horizontalalignment='center',
         fontsize=font_size,
         transform = ax1.transAxes)

# Subplot 2,2,2  grasp: start-end
data = [list(exp1.grasp_start_sp.values),list(exp1.grasp_end_sp.values)]
ax2 = fig.add_subplot(2, 2, 2)
cumming_plot.paired(data,ax2,
                    yticks=[-10, 20, 5],
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
plt.text(0.5, 1.08, 'Grasp',
         horizontalalignment='center',
         fontsize=font_size,
         transform = ax2.transAxes)

x_axis_nudge = [-0.005, -0.0075, -.005]

# Subplot 2,2,3  start: no-grasp grasp
data = [list(exp1.no_grasp_start_sp.values),list(exp1.grasp_start_sp.values)]
ax3 = fig.add_subplot(2, 2, 3)
cumming_plot.paired(data,ax3,
                    yticks=[-10, 20, 5],
                    style=style3,
                    ylabel='Perceived spacing (cm)',
                    xlabel=['no grasp', 'grasp', 'effect'],
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
         transform = ax3.transAxes)
plt.text(0.5, 1.08, 'Start',
         horizontalalignment='center',
         fontsize=font_size,
         transform = ax3.transAxes)

# Subplot 2,2,4  end: no-grasp grasp
data = [list(exp1.no_grasp_end_sp.values),list(exp1.grasp_end_sp.values)]
ax4 = fig.add_subplot(2, 2, 4)
cumming_plot.paired(data,ax4,
                    yticks=[-10, 20, 5],
                    style=style4,
                    xlabel=['no grasp', 'grasp', 'effect'],
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
plt.text(0.5, 1.08, 'End',
         horizontalalignment='center',
         fontsize=font_size,
         transform = ax4.transAxes)

# Adjust spacing of subplots
left  = 0.1
right = 0.9
bottom = 0.05
top = 0.92
wspace = 0.5   # the amount of width reserved for blank space between subplots
hspace = 0.5   # the amount of height reserved for white space between subplots
fig.subplots_adjust(left=left, bottom=bottom, right=right, top=top, wspace=wspace, hspace=hspace)

#plt.savefig('figure3.pdf', format='pdf', dpi=600)
plt.savefig('figure3.png', format='png', dpi=600)
plt.savefig('figure3.svg', format='svg', dpi=600)

##########
# Figure 4
##########

fig = plt.figure(figsize=[2.5, 6])

# Subplot 3,1,1 ownership results
style1 = {'a': ['o', 'w', 'k'], 'b': ['o', 'w', 'k'], 'diff': ['^', 'k', 'k']}
style2 = {'a': ['o', 'w', 'k'], 'b': ['o', 'w', 'k'], 'diff': ['^', 'k', 'k']}
style3 = {'a': ['o', 'w', 'k'], 'b': ['o', 'w', 'k'], 'diff': ['^', 'k', 'k']}
style4 = {'a': ['o', 'w',  'k'], 'b': ['o', 'w', 'k'], 'diff': ['^', 'k', 'k']}
marker_size = [2, 4]
markeredgewdith = 1
linewidth = 1
axes_tick_width = 0.5
font_size = 8
letterfontsize = 10
connectcolor = '0.8'
x_spacing = [0.01, 0.015, 0.05, 0.055, 0.075]
jit=0.0001
skip_raw_marker=True
x_axis_nudge = [-0.005, -0.005, -.005]
zero_line2 = False
likert_items = ['1','2','3','4','5','6','7']
letters = [-0.3, 1.1]

data = [list(exp1.grasp_start_own.values),list(exp1.grasp_end_own.values)]
ax1 = fig.add_subplot(3, 1, 1)
cumming_plot.paired(data,ax1,
                    style=style1,
                    ylabel='Perceived ownership',
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
                    likert=True,
                    likert_items=likert_items,
                    skip_raw_marker=skip_raw_marker,
                    x_axis_nudge=x_axis_nudge,
                    zero_line2=zero_line2)
plt.text(letters[0], letters[1], 'A',
         horizontalalignment='center',
         fontsize=letterfontsize,
         transform = ax1.transAxes)

# subplot 3,1,2  correlation start spacing-ownership
marker_size = [1, 4]

a = exp1['grasp_start_own']
b = exp1['grasp_start_sp']

duplicate_one = []
duplicate_two = []
duplicate_three = []
duplicate_four = []
duplicate_five = []
duplicate_six = []
duplicate_seven = []
jit = 0.05
jitter_a = [''] * len(a)
jitter_a[0] = 0

for i in np.arange(0, len(a), 1):
    a_val = a.values[i]
    b_val = b.values[i]
    if a_val == 1:
        if b_val in duplicate_two:
            num_times = duplicate_two.count(b_val)
            jitter_a[i] = a_val + (jit * num_times)
            duplicate_two.append(b_val)
        else:
            duplicate_two.append(b_val)
            jitter_a[i] = a_val
    elif a_val == 2:
        if b_val in duplicate_two:
            num_times = duplicate_two.count(b_val)
            jitter_a[i] = a_val + (jit * num_times)
            duplicate_two.append(b_val)
        else:
            duplicate_two.append(b_val)
            jitter_a[i] = a_val
    elif a_val == 3:
        if b_val in duplicate_two:
            num_times = duplicate_two.count(b_val)
            jitter_a[i] = a_val + (jit * num_times)
            duplicate_two.append(b_val)
        else:
            duplicate_two.append(b_val)
            jitter_a[i] = a_val
    elif a_val == 4:
        if b_val in duplicate_two:
            num_times = duplicate_two.count(b_val)
            jitter_a[i] = a_val + (jit * num_times)
            duplicate_two.append(b_val)
        else:
            duplicate_two.append(b_val)
            jitter_a[i] = a_val
    elif a_val == 5:
        if b_val in duplicate_two:
            num_times = duplicate_two.count(b_val)
            jitter_a[i] = a_val + (jit * num_times)
            duplicate_two.append(b_val)
        else:
            duplicate_two.append(b_val)
            jitter_a[i] = a_val
    elif a_val == 6:
        if b_val in duplicate_two:
            num_times = duplicate_two.count(b_val)
            jitter_a[i] = a_val + (jit * num_times)
            duplicate_two.append(b_val)
        else:
            duplicate_two.append(b_val)
            jitter_a[i] = a_val
    elif a_val == 7:
        if b_val in duplicate_two:
            num_times = duplicate_two.count(b_val)
            jitter_a[i] = a_val + (jit * num_times)
            duplicate_two.append(b_val)
        else:
            duplicate_two.append(b_val)
            jitter_a[i] = a_val


ax2 = fig.add_subplot(3, 1, 2)
ax2.plot(jitter_a, b, marker='o', color='k',
            markeredgecolor='k',  markersize=marker_size[0],
            markeredgewidth=1, linestyle='None')

ax2.tick_params(width=axes_tick_width, axis='both', colors='k')
ax2.tick_params(axis='x', which='both', bottom='on',
                   top='off', labelbottom='on')
ax2.tick_params(axis='y', right='off', labelbottom='on')
ax2.tick_params(axis='y', which='both', labelsize=font_size)
ax2.tick_params(axis='x', which='both', labelsize=font_size)
ax2.spines['left'].set_linewidth(axes_tick_width)
ax2.spines['bottom'].set_linewidth(axes_tick_width)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

ax2.set_ylim ([-5, 15.5])
ax2.set_xlim ([0.5, 7.5])
ax2.set_ylabel('Perceived spacing (cm)',fontsize=font_size)
ax2.set_xlabel('Perceived ownership',fontsize=font_size)

plt.text(letters[0], letters[1], 'B',
         horizontalalignment='center',
         fontsize=letterfontsize,
         transform = ax2.transAxes)

fit = np.polyfit(exp1['grasp_start_own'], exp1['grasp_start_sp'], 1)
fit_fn = np.poly1d(fit)

import scipy.stats
rho, p = scipy.stats.spearmanr(exp1['grasp_start_own'], exp1['grasp_start_sp'])
r, p = scipy.stats.pearsonr(exp1['grasp_start_own'], exp1['grasp_start_sp'])

# subplot 3,1,3  correlation end spacing-ownership
a = exp1['grasp_end_own']
b = exp1['grasp_end_sp']

duplicate_one = []
duplicate_two = []
duplicate_three = []
duplicate_four = []
duplicate_five = []
duplicate_six = []
duplicate_seven = []
jitter_a = [''] * len(a)
jitter_a[0] = 0

for i in np.arange(0, len(a), 1):
    a_val = a.values[i]
    b_val = b.values[i]
    if a_val == 1:
        if b_val in duplicate_two:
            num_times = duplicate_two.count(b_val)
            jitter_a[i] = a_val + (jit * num_times)
            duplicate_two.append(b_val)
        else:
            duplicate_two.append(b_val)
            jitter_a[i] = a_val
    elif a_val == 2:
        if b_val in duplicate_two:
            num_times = duplicate_two.count(b_val)
            jitter_a[i] = a_val + (jit * num_times)
            duplicate_two.append(b_val)
        else:
            duplicate_two.append(b_val)
            jitter_a[i] = a_val
    elif a_val == 3:
        if b_val in duplicate_two:
            num_times = duplicate_two.count(b_val)
            jitter_a[i] = a_val + (jit * num_times)
            duplicate_two.append(b_val)
        else:
            duplicate_two.append(b_val)
            jitter_a[i] = a_val
    elif a_val == 4:
        if b_val in duplicate_two:
            num_times = duplicate_two.count(b_val)
            jitter_a[i] = a_val + (jit * num_times)
            duplicate_two.append(b_val)
        else:
            duplicate_two.append(b_val)
            jitter_a[i] = a_val
    elif a_val == 5:
        if b_val in duplicate_two:
            num_times = duplicate_two.count(b_val)
            jitter_a[i] = a_val + (jit * num_times)
            duplicate_two.append(b_val)
        else:
            duplicate_two.append(b_val)
            jitter_a[i] = a_val
    elif a_val == 6:
        if b_val in duplicate_two:
            num_times = duplicate_two.count(b_val)
            jitter_a[i] = a_val + (jit * num_times)
            duplicate_two.append(b_val)
        else:
            duplicate_two.append(b_val)
            jitter_a[i] = a_val
    elif a_val == 7:
        if b_val in duplicate_two:
            num_times = duplicate_two.count(b_val)
            jitter_a[i] = a_val + (jit * num_times)
            duplicate_two.append(b_val)
        else:
            duplicate_two.append(b_val)
            jitter_a[i] = a_val


ax3 = fig.add_subplot(3, 1, 3)
ax3.plot(jitter_a, b, marker='o', color='k',
            markeredgecolor='k',  markersize=marker_size[0],
            markeredgewidth=1, linestyle='None')

ax3.tick_params(width=axes_tick_width, axis='both', colors='k')
ax3.tick_params(axis='x', which='both', bottom='on',
                   top='off', labelbottom='on')
ax3.tick_params(axis='y', right='off', labelbottom='on')
ax3.tick_params(axis='y', which='both', labelsize=font_size)
ax3.tick_params(axis='x', which='both', labelsize=font_size)
ax3.spines['left'].set_linewidth(axes_tick_width)
ax3.spines['bottom'].set_linewidth(axes_tick_width)
ax3.spines['top'].set_visible(False)
ax3.spines['right'].set_visible(False)

ax3.set_ylim ([-5, 15.5])
ax3.set_xlim ([0.5, 7.5])
ax3.set_ylabel('Perceived spacing (cm)',fontsize=font_size)
ax3.set_xlabel('Perceived ownership',fontsize=font_size)

plt.text(letters[0], letters[1], 'C',
         horizontalalignment='center',
         fontsize=letterfontsize,
         transform = ax3.transAxes)

fit = np.polyfit(exp1['grasp_end_own'], exp1['grasp_end_sp'], 1)
fit_fn = np.poly1d(fit)
ax3.plot(exp1['grasp_end_own'], fit_fn(exp1['grasp_end_own']), linestyle='-',
         color='k',linewidth=linewidth)

rho, p = scipy.stats.spearmanr(exp1['grasp_end_own'], exp1['grasp_end_sp'])
r, p = scipy.stats.pearsonr(exp1['grasp_end_own'], exp1['grasp_end_sp'])

# Fix spacing between subplots
left  = 0.4
right = 0.9
bottom = 0.1
top = .95
wspace = 0.4   # the amount of width reserved for blank space between subplots
hspace = 0.5   # the amount of height reserved for white space between subplots
fig.subplots_adjust(left=left, bottom=bottom, right=right, top=top, wspace=wspace, hspace=hspace)

#plt.savefig('figure4.pdf', format='pdf', dpi=600)
plt.savefig('figure4.png', format='png', dpi=600)
plt.savefig('figure4.svg', format='svg')
