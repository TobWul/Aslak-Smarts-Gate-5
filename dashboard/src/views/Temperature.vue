<template>
    <div id="temperature">
        <h1>Temperaturer</h1>
        <button @click="sendTemp()">Send temperatur</button>
        <div class="card">
            <temperature-chart
                    v-if="!loaded"
                    :chartData="chartData"/>
        </div>
	<div v-for="(temp, index) of temperatures">
		{{timestamps[index]}}: {{temp}}
	</div>
    </div>
</template>
<script>
    import TemperatureChart from "../components/TemperatureChart";
    import axios from 'axios'
    import {HTTP} from "@/assets/js/http-common";

    export default {
        name: 'temperature',
        components: {TemperatureChart},
        data() {
            return {
                temperatures: [],
                timestamps: [],
                loaded: false,
                chartData: {
                    labels: this.timestamps,
                    datasets: [
                        {
                            label: 'Temperature',
                            backgroundColor: '#ffffff',
                            data: this.temperatures
                        }
                    ]
                }
            }
        },
        methods: {
            sendTemp: function() {
                HTTP.post('inside-temperatures/', {
                    timestamp: "2019-03-17T15:58:50Z",
                    temperature: 22.1
                })
                .then(response => {})
                .catch(e => {
                    console.log(e);
                })
            },
          convertTemperatures: function(temperatures) {
              for (let i = 0; i < temperatures.length; i++) {
                  let time = new Date(temperatures[i].timestamp)
                  this.timestamps.push(`${time.getHours()}:${time.getMinutes()}`);
                  this.temperatures.push(temperatures[i].temperature);
              }
              console.log(this.timestamps, this.temperatures)
          }
        },
        mounted() {
		HTTP.get('inside-temperatures/')
                .then((response) => (
                    this.convertTemperatures(response.data)
                ))
        }
    }
</script>
