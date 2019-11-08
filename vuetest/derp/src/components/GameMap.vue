<template>
  <div id="mapboxmap">
    <mapbox
      access-token="your access token"
      :map-options="{
        style: 'mapbox://styles/mapbox/light-v9',
        center: [-96, 37.8],
        zoom: 3,
      }"
    />
  </div>
</template>

<script>
import Mapbox from 'mapbox-gl-vue'

export default {
  components: { Mapbox },
}
</script>

<style>
    body{
        background-color:#ff0000;
    }
</style>
