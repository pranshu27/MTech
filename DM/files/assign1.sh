SECONDS=0


bash scripts/case-generator.sh   
echo "executed case-generator.sh"

duration=$SECONDS
echo "$(($duration / 60)) minutes and $(($duration % 60)) seconds elapsed."
echo ""

bash scripts/complete-vaccination-generator.sh  
echo "executed complete-vaccination-generator.sh"

duration=$SECONDS
echo "$(($duration / 60)) minutes and $(($duration % 60)) seconds elapsed."
echo ""
bash scripts/edge-generator.sh                  
echo "executed edge-generator.sh"

duration=$SECONDS
echo "$(($duration / 60)) minutes and $(($duration % 60)) seconds elapsed."
echo ""
bash scripts/peaks-generator.sh
echo "executed peaks-generator.sh"

duration=$SECONDS
echo "$(($duration / 60)) minutes and $(($duration % 60)) seconds elapsed."
echo ""
bash scripts/vaccinated-count-generator.sh
echo "executed vaccinated-count-generator.sh"

duration=$SECONDS
echo "$(($duration / 60)) minutes and $(($duration % 60)) seconds elapsed."
echo ""
bash scripts/vaccinated-ratio-generator.sh 
echo "executed vaccinated-ratio-generator.sh"

duration=$SECONDS
echo "$(($duration / 60)) minutes and $(($duration % 60)) seconds elapsed."
echo ""
bash scripts/vaccination-population-ratio-generator.sh
echo "executed vaccination-population-ratio-generator.sh"

duration=$SECONDS
echo "$(($duration / 60)) minutes and $(($duration % 60)) seconds elapsed."
echo ""
bash scripts/vaccine-type-ratio-generator.sh
echo "executed vaccine-type-ratio-generator.sh"
echo ""
duration=$SECONDS
echo "$(($duration / 60)) minutes and $(($duration % 60)) seconds elapsed."
echo ""
echo "Finished. Please check the 'output' directory for the resultant CSV files."
