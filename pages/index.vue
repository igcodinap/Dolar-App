<script>
import VueCharts from 'vue-chartjs'
import { Line, mixins } from 'vue-chartjs'
import axios from 'axios'

export default {
  mixins: [mixins.reactiveData],
  data() {
    return {
      chartData: '',
    }
  },
  extends: Line,
  mounted() {
    this.renderChart(this.chartData)
  },
  created() {
    axios.get('http://127.0.0.1:8000/api/dolar/')
      .then(response => {
        // JSON responses are automatically parsed.
        const responseData = response.data
        this.chartData = {
          labels: responseData.map(item => item.fecha),
          datasets: [{
            label: 'Variacion diaria del dolar',
             backgroundColor: '#f87979',
             data: responseData.map(item => item.valor)
            }]
          };
        }
      )
      .catch(e => {
        this.errors.push(e)
      })
    }
  }
</script>
