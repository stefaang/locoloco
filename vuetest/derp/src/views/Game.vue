<template>
  <div id="map">
    <MglMap :accessToken="accessToken"
            :mapStyle="mapStyle"
            :center="mapCenter"
            :zoom="defaultZoom"
            :dragRotate=false
            @load="onMapLoad">
      <MglNavigationControl :showZoom="true" :showCompass="false" />

    </MglMap>
  </div>
</template>

<script>
import Mapbox from 'mapbox-gl'
import { MglMap, MglNavigationControl } from 'vue-mapbox'

export default {
  components: {
    MglMap,
    MglNavigationControl
  },
  data () {
    return {
      accessToken: process.env.VUE_APP_MAPBOX_TOKEN, // your access token. Needed if you using Mapbox maps
      defaultZoom: 12,
      mapCenter: [3.735, 51.015],
      mapStyle: 'mapbox://styles/mapbox/streets-v9' // your map style

    }
  },
  methods: {
    async onMapLoad(event) {
    // Actions to run when the map is loaded
      const asyncActions = event.component.actions

      const newParams = await asyncActions.flyTo({
        zoom: 16,
        pitch: 45,
        speed: 1
      })
      console.log(newParams)
    }
  },
  created () {
    // We need to set mapbox-gl library here in order to use it in template
    this.mapbox = Mapbox
  }
}
</script>

<style scoped lang="scss">

  /*@import '../assets/css/mapbox-gl.css';*/
  #map {
    padding: 30px;
    width: 100%;
    height: 500px;
  }

</style>


