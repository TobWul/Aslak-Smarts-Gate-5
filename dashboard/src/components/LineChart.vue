<script>
    import { Line, mixins } from 'vue-chartjs'
    const { reactiveProp } = mixins
    export default {
        extends: Line,
        mixins: [reactiveProp],
        data() {
            return {
                options: {
                    scales: {
                        yAxes: [{
                          ticks: {
                              beginAtZero: false,
                              fontColor: 'white'
                          },
                            gridLines: {
                              display: true
                            }
                        }],
                        xAxes: [{
                            ticks: {
                                fontColor: 'white'
                            },
                            gridLines: {
                                display: false
                            }
                        }]
                    },
                    legend: {
                        display: true,
                        labels: {
                            fontColor: 'white'
                        },
                    },
                    responsive: true,
                    maintainAspectRatio: false
                }
            }
        },
        mounted() {
            this.renderChart(this.chartData, this.options)
        }
    }
</script>