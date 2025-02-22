import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style='darkgrid')

class Plotter_Helper:

    @classmethod
    def box_hist_plot(cls, x, save_path):
        
        f, ax_box, ax_hist = cls.sub_plots()

        sns.boxplot(x=x, ax=ax_box, showmeans=True, color='purple')
        sns.histplot(x=x, kde=False, ax=ax_hist, bins="auto")
        ax_hist.axvline(x.mean(), color='g', linestyle='--')      # Add mean to the histogram
        ax_hist.axvline(x.median(), color='black', linestyle='-') # Add median to the histogram

        
        plt.savefig(save_path)

    @classmethod
    def heatmapper(cls,coor_df, save_path, cmap='coolwarm', annot=True, figsize=(14,10), fmt=".1f"):
        
        plt.figure(figsize = figsize)

        sns.heatmap(coor_df, annot = annot, cmap = cmap,            
        fmt = fmt,            
        xticklabels = coor_df.columns,            
        yticklabels = coor_df.columns)

        plt.savefig(save_path)

    @classmethod
    def lineplot(cls,df, x,y,save_path, ci=0,color="PURPLE", estimator = "sum",figsize=(20,7), x_label = None, y_label = None):

        plt.figure(figsize = figsize)
        sns.lineplot(x = x, y=y, data=df, errorbar=('ci', ci)
                     , color = color, estimator = estimator)
        plt.ylabel(y if y_label is None else y_label)
        plt.xlabel(x if x_label is None else x_label)
        plt.savefig(save_path)

    @classmethod
    def barplot(cls, data, feature, save_path, perc=False, top_n = None):
        total = len(data[feature])
        count = data[feature].nunique()
        f = (count+1,5) if top_n is None else (top_n+1,5)
        plt.figure(figsize=f)
        
        plt.xticks(rotation=90, fontsize=15)
        ax = sns.countplot(
                            data = data,
                            x = feature,
                            palette = "Paired",
                            order = data[feature].value_counts().index[:top_n].sort_values(),
                            )
        for p in ax.patches:
           
            label = "{:.1f}%".format(100 * p.get_height() / total)  if perc else p.get_height() 
                                    
            x = p.get_x() + p.get_width() / 2  # Width of the plot
            y = p.get_height()                 # Height of the plot

            ax.annotate(
                label,
                (x, y),
                ha = "center",
                va = "center",
                size = 12,
                xytext = (0, 5),
                textcoords = "offset points",
            )  # Annotate the percentage
        plt.savefig(save_path)


        
    @classmethod
    def sub_plots(cls, nrows = 2,  gridspec_kw = {"height_ratios": (.25, .75)}
                  , figsize = (15,10)):
        
        f, (ax_box, ax_hist) = plt.subplots(
        nrows = nrows,  # Number of rows of the subplot grid
        sharex = True,  # The X-axis will be shared among all the subplots
        gridspec_kw = gridspec_kw,
        figsize = figsize)

        return f, ax_box, ax_hist