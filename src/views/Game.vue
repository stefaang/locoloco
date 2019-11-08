<template>
  <MglMap :accessToken="accessToken"
          :mapStyle="mapStyle"/>
</template>

<script>
import Mapbox from 'mapbox-gl'
import { MglMap } from 'vue-mapbox'

export default {
  components: {
    MglMap
  },
  data () {
    return {
      accessToken: 'pk.eyJ1IjoidGhnaCIsImEiOiJjaXdlMTJiczkwMDZ6MnRvNmdjODNmOTBlIn0.8aeMZVbu2uuPDXKcpDmZVw', // your access token. Needed if you using Mapbox maps
      mapStyle: 'mapbox://styles/mapbox/streets-v9' // your map style
    }
  },

  created () {
    // We need to set mapbox-gl library here in order to use it in template
    this.mapbox = Mapbox
  }
}
</script>
