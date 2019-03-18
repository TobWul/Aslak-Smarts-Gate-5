module.exports = {
    css: {
        loaderOptions: {
            sass: {
                data: `
                    @import "public/scss/global/_variables.scss";
                    @import "public/scss/global/_mixins.scss";
                `
            }
        }
    }
};
