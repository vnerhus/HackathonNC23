<template>
    <h1>Lunsjmeny</h1>
    <h2>Uke 6: Mandag</h2>
    <el-table :data="tableData" style="width: 100%">
      <el-table-column prop="date" label="Type" width="180" />
      <el-table-column prop="name" label="Lunsjbeskrivelse" />
    </el-table>
</template>
  
<script lang="ts" setup>
  const tableData = [
    {
      date: 'Lunsj',
      name: 'Kylling korma med raita,  mangochutney og nan basmatiris(melk, hvete,  cashewnøt, hvitløk)',
    },
    {
      date: 'Lunsj veg',
      name: 'Palak paneer m rita mangochutny basmatiris nan (melk, hvete,  sulfit)',
    },
    {
      date: 'Dagens påsmurt',
      name: 'Langpanne rotspelt,  med serrano,  syltarødløk,  brie og aioli. (hvete,  egg,  sennep,  sulfitt,  hvitløk,  melk)',
    },
    {
      date: 'Dagens påsmurt veg',
      name: 'Langpanne rotspelt,  med tomat,  syltarødløk,  brie og aioli. (hvete,  egg,  sennep,  sulfitt,  hvitløk,  melk)',
    },
    {
      date: 'Dagens salat',
      name: 'Bulgursalat marinert bulgur med og grønnsaksmix,  med grillet svinenakke. Syltet rødløk. (hvete,  sulfitt)',
    },
    {
      date: 'Dagens salat veg',
      name: 'Bulgursalat,  marinert bulgur og grønnsaksmix,  med feta ,  oliven og Syltet rødløk. (hvete,  melk,  sulfitt)',
    },
  ]
</script>
  