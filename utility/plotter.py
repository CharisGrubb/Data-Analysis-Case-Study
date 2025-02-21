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
    def sub_plots(cls, nrows = 2,  gridspec_kw = {"height_ratios": (.25, .75)}
                  , figsize = (15,10)):
        
        f, (ax_box, ax_hist) = plt.subplots(
        nrows = nrows,  # Number of rows of the subplot grid
        sharex = True,  # The X-axis will be shared among all the subplots
        gridspec_kw = gridspec_kw,
        figsize = figsize)

        return f, ax_box, ax_hist